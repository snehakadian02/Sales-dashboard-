import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Category": ["Electronics", "Electronics", "Clothing", "Clothing", "Electronics", "Clothing"],
    "Sales": [5000, 6500, 4000, 5500, 7000, 6000]
}

df = pd.DataFrame(data)

st.subheader("Sales Data")
st.dataframe(df)

category = st.selectbox("Choose a Category", df["Category"].unique())

filtered_df = df[df["Category"] == category]

st.metric("Total Sales", filtered_df["Sales"].sum())

fig = px.bar(
    filtered_df,
    x="Month",
    y="Sales",
    color="Month",
    title="Monthly Sales"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.line(
    filtered_df,
    x="Month",
    y="Sales",
    markers=True,
    title="Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)

