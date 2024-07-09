import streamlit as st
import pandas as pd
import prepocessor,helper

df=prepocessor.preprocess()
st.sidebar.title('Olympics Analysis')
user_menu=st.sidebar.radio('select an option',('Medal Tally','overall analysis','Country-wise analysis','athlete wise analysis'))

if user_menu=='Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox('selected years',years)
    selected_country = st.sidebar.selectbox('selected country', country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country )
    st.dataframe(medal_tally)
