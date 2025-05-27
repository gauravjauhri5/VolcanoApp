import streamlit as st  # type: ignore
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from copy import deepcopy

@st.cache_data   
def load_data(path):
    df = pd.read_csv(path)
    return df

@st.cache_data   
def load_json(path):
    df = json.load(open(path))
    return df


vol_df = load_data('./volcano_ds_pop.csv')
vol_json = load_json('./countries.geojson')

# st.table(data=mpg_df)
if st.checkbox("Show Dataframe"):

    st.subheader("This is my dataset:")
    st.dataframe(data=vol_df)

#left_column, right_column = st.columns(2)
left_column, middle_column = st.columns([3, 3])

countries = ["All"]+sorted(pd.unique(vol_df['Country']))
country = left_column.selectbox("Choose a Country", countries)



if country == "All":
    reduced_df = vol_df
else:
    reduced_df = vol_df[vol_df["Country"] == country]

status = ["All"]+sorted(pd.unique(reduced_df['Status']))
stat = middle_column.selectbox("Choose Volcano Status", status)


if stat == "All":
    reduced_df = reduced_df
else:
    reduced_df = reduced_df[reduced_df["Status"] == stat]


reduced_df.rename(columns={'Latitude' : 'lat', 'Longitude' : 'lon'}, inplace= True)

st.title('Volcano Distribution around the world')

st.map(reduced_df)


