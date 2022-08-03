import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open("logo.png")
st.image(image)
st.text('Jornada de Dados - Victor Barros')

df = pd.read_csv("Etapa 4 - dataframe_final.csv")
candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('candidato', candidato_unico, candidato_unico)

df_candidato_selecionado = df[(df['Candidato'].isin(selecionar_candidato))]

st.dataframe(df_candidato_selecionado)