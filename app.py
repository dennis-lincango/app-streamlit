import streamlit as st
import requests
from config import URL

# Título de la app
st.title("Demo clasificador de Mensajes con Flask")

# Entrada de texto
mensaje = st.text_area("Ingrese un mensaje para clasificar:", "")

API_URL = URL

# Botón de envío
if st.button("Clasificar"):
    if mensaje.strip():
        try:
            respuesta = requests.get(f"{API_URL}{mensaje}")
            if respuesta.status_code == 200:
                resultado = respuesta.json()
                st.success(f"FRASE: {mensaje} - Predicción: {resultado['prediction'][0]}")
            else:
                st.error(f"Error al conectar: {respuesta.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Por favor, ingrese un mensaje.")
