import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

st.title("Dashboard afluencia de clientes - Cafe internet")

dfCafe = pd.read_excel("datos/resultadoLimpieza.xlsx")
anios = list(set(dfCafe['fechaEntrada'].dt.year))
mes = list(set(dfCafe['fechaEntrada'].dt.month_name()))
mes_sorted = list(calendar.month_name)

st.title("-Filtros-")

anioSelect = st.sidebar.selectbox('Seleccionar año', anios)
mesSelect = st.sidebar.selectbox('Seleccionar Mes', mes_sorted)

dfFiltradoMesanio = dfCafe[(dfCafe['fechaEntrada'].dt.month_name() == mesSelect) & (dfCafe['fechaEntrada'].dt.year == anioSelect)]
dfMes = dfFiltradoMesanio.groupby(pd.Grouper(key='fechaEntrada', freq="1D")).count().reset_index()
dfMes['fechaStr'] = dfMes['fechaEntrada'].astype(str) + " - "
dfMes['Día'] = dfMes['fechaEntrada'].dt.day_name() + " - " + dfMes['fechaStr']


fig = px.bar(dfMes, x='Día', y='horaEntrada', labels={'horaEntrada':'Número de Clientes'}, title="Número de Clientes por semana")
st.plotly_chart(fig,use_container_width=True)
