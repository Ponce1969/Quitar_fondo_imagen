import streamlit as st
from PIL import Image
from rembg import remove 
import io
import time

# Función para procesar la imagen y quitar el fondo
def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    return remove_background(image)

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    processed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image_bytes))

# Configuración de la aplicación Streamlit
st.image("assets/camaroremove.png")
st.header("APP Quitar Fondo de Imagen")
st.subheader("Subir la Imagen")

uploaded_image = st.file_uploader("Selecciona una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Imagen original", use_column_width=True)
    remove_button = st.button(label="Quitar fondo")

    if remove_button:
        progress_text = st.empty()
        progress_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.05)
            progress_text.text(f"Procesando: {percent_complete + 1}%")
            progress_bar.progress(percent_complete + 1)

        processed_image = process_image(uploaded_image)
        st.image(processed_image, caption="Imagen sin fondo", use_column_width=True)

        image_byte = io.BytesIO()
        processed_image.save(image_byte, format="PNG")
        image_byte.seek(0)
        st.download_button("Descargar imagen procesada", data=image_byte.getvalue(), file_name="processed_image.png")

st.markdown("""
    <style>
        .footer {
            color: #4A90E2;    /* Cambia esto al color que prefieras para el texto */
            font-size: 16px;
            padding: 20px 10px;
            text-align: center;
            border-top: 2px solid #4A90E2;   /* Cambia esto al color que prefieras para la línea */
            width: 100%;
            left: 0;
            position: relative;
            background-color: #FAFAFA;   /* Cambia esto al color que prefieras para el fondo */
            margin-top: 50px;
        }
        .footer a {
            color: #4A90E2;    /* Cambia esto al color que prefieras para los enlaces */
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Añadimos el footer estilizado
st.markdown("""
    <div class="footer">
        Esta aplicación utiliza la biblioteca rembg para quitar el fondo de las imágenes. 
        Fue creada con ❤️ por <a href="#" target="_blank">Gonzalo Ponce</a>.
    </div>
    """, unsafe_allow_html=True)