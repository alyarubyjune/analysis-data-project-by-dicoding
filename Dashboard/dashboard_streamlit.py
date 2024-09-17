import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv('data.csv')
order_df = pd.read_csv('order_count_by_category.csv')
revenue_df = pd.read_csv('total_revenue_by_category.csv')
city_df = pd.read_csv("customer_count_by_city.csv")

st.header('E-commerce Public Data Viz')

# TOP SALES
st.subheader('Best and Worst Performing Product')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 20))
colors = ['#90CAF9', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']

sns.barplot(x='order_count', y='product_category_name_english', data=order_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel('Number of Sales', fontsize=35)
ax[0].set_title('Best Performing Product', loc='center', fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=35)

sns.barplot(x='order_count', y='product_category_name_english', data=order_df.sort_values(by='order_count', ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel('Number of Sales', fontsize=35)
ax[1].set_title('Worst Performing Product', loc='center', fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=35)

plt.tight_layout()
st.pyplot(fig)

# TOP REVENUE
st.subheader('Top 10 Total Revenue')
fig, ax = plt.subplots(figsize=(35, 20))
colors = ['#90CAF9', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']

sns.barplot(x='total_revenue', y='product_category_name_english', data=revenue_df.head(10), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel('Number of Revenue (million)', fontsize=35)
ax.set_title('Highest Revenue Product', loc='center', fontsize=50)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=35)

plt.tight_layout()
st.pyplot(fig)

# TOP CUSTOMER CITY
st.subheader('Top 10 City')
fig, ax = plt.subplots(figsize=(35, 20))
colors = ['#90CAF9', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']

sns.barplot(x='city_count', y='customer_city', data=city_df.head(5), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel('Number of Customer', fontsize=35)
ax.set_title('Customer by City', loc='center', fontsize=50)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=35)

plt.tight_layout()
st.pyplot(fig)