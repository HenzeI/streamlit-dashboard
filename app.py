"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Título principal")
st.header("Encabezado")
st.subheader("Subtítulo")
st.write("Texto normal o variables")


nombre = st.text_input("Introduce tu nombre")
edad = st.number_input("Edad", min_value=0, max_value=120)
opcion = st.selectbox("Elige una opción", ["A", "B", "C"])
mostrar = st.checkbox("Mostrar datos")


if st.button("Procesar"):
    st.success("Botón pulsado")


df = pd.DataFrame({
"A": [1,2,3],
"B": [4,5,6]
})
st.dataframe(df)


fig, ax = plt.subplots()
ax.plot([1,2,3], [4,5,6])
st.pyplot(fig)


fig = px.line(df, x="A", y="B")
st.plotly_chart(fig)


with st.sidebar:
    st.header("Opciones")
    filtro = st.selectbox("Filtro", ["Opción 1", "Opción 2"])


col1, col2 = st.columns(2)
col1.metric("Ventas", "1200€", "+5%")
col2.metric("Clientes", "320", "-2%")


tab1, tab2 = st.tabs(["Gráfico", "Tabla"])
with tab1:
    st.write("Aquí va el gráfico")
with tab2:
    st.write("Aquí va la tabla")


archivo = st.file_uploader("Sube un CSV", type="csv")
if archivo:
    df = pd.read_csv(archivo)
    st.dataframe(df)
"""


import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Ventas")

# Sidebar
with st.sidebar:
    st.header("Filtros")
    year = st.selectbox("Año", [2022, 2023, 2024])

# Datos de ejemplo
df = pd.DataFrame({
    "Año": [2022, 2022, 2023, 2023, 2024, 2024],
    "Mes": ["Ene","Feb","Ene","Feb","Ene","Feb"],
    "Ventas": [100,150,200,180,250,300]
})

df_filtrado = df[df["Año"] == year]

# Métricas
st.metric("Ventas totales", f"{df_filtrado['Ventas'].sum()} €")

# Gráfico
fig = px.bar(df_filtrado, x="Mes", y="Ventas", title="Ventas por mes")
st.plotly_chart(fig)
# Tabla
st.dataframe(df_filtrado)
