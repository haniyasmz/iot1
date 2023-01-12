'''
Created on 12 Jan 2023

@author: hanimurnizam
'''

import streamlit as st
import pandas as pd
import psycopg2

st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

# streamlit_app.py


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from sanitizer_records;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
