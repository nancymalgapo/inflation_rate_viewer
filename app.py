import pandas as pd
import streamlit as st
import plotly.express as plt

dataset = "files/global_inflation_data.csv"
df = pd.read_csv(dataset)

st.title("Inflation Rate Visualization")

countries = df["Country"].unique()
selected_country = st.selectbox("Select a Country: ", countries)

country_data = df[df["Country"] == selected_country].set_index("Country")
inflation_rates = country_data.T

plot_df = inflation_rates.reset_index()
plot_df.columns = ["Year", "Inflation Rate"]
fig = plt.line(
        plot_df,
        x="Year",
        y="Inflation Rate",
        title=f"Inflation Trend in {selected_country} from 1980 to 2024",
        markers=True
)
st.plotly_chart(fig)

if st.checkbox("Show raw data"):
        st.write(inflation_rates)
