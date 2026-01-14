import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
data = pd.read_csv("data/merged_games.csv")  # Merge output from notebook

st.title("Video Game Sales & Engagement Dashboard (Mini Project)")

# Top-rated games
st.header("Top Rated Games")
top_rated = data.sort_values("Rating", ascending=False).head(10)
st.bar_chart(top_rated.set_index("Title")["Rating"])

# Top-selling platforms
st.header("Top-Selling Platforms")
platform_sales = data.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
st.bar_chart(platform_sales)

# Ratings vs Global Sales
st.header("Ratings vs Global Sales")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="Rating", y="Global_Sales", hue="Genre", ax=ax)
st.pyplot(fig)
