import streamlit as st
import pandas as pd
import altair as alt

st.header("Problematische Netzwerke - Messenger-Dienste")
st.subheader("Anteil der Befragten, die auf problematische Inhalte gestoßen sind")

source = pd.DataFrame({
        'Anteil(%)': [73, 43, 39, 37, 26],
        'Art der problematischen Inhalte': ['Falsche Informationen', 'Manipulative Inhalte', 'Verletzende Inhalte', 'Hetzerische Inhalte', 'Bedrohliche Inhalte']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Art der problematischen Inhalte:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=1053; Ab 18 Jahre; Deutschland; Dezember 2022
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: BMJV/ConPolicy")