import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data_path = './data/23_24_premier_league_0408_general.csv'
title = ':soccer: Soccer - Premier League 2023/24'
paragraph = '''
    This is the homepage of the Premier League 2023/24 season. 
    The data includes general information about the teams and players in the league. 
    '''
# Add a title and a paragraph
st.header(title)
st.write('---')
st.write(paragraph)

# Load the data and display table
soccer_db = pd.read_csv(data_path)
st.write(soccer_db)

# Create a bar plot
soccer_db_sorted = soccer_db.sort_values('league_position')
plt.figure(figsize=(10, 6))
plt.bar(soccer_db_sorted['squad'], soccer_db_sorted['Home_GF'], color='blue')
plt.xlabel('Squad')
plt.ylabel('Home Goals For')
plt.title('Home Goals For by Team Ordered by League Position')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

st.write('---')

# Create an interactive bar plot
fig = px.bar(soccer_db_sorted, x='squad', y='Home_GF',
             title='Home Goals For by Team Ordered by League Position',
             labels={'squad': 'Squad', 'Home_GF': 'Home Goals For'},
             color='Home_GF', color_continuous_scale=px.colors.sequential.Viridis)

# Display the plot in Streamlit
st.plotly_chart(fig)


