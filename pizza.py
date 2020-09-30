import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown('Hey there, this is just a test for the new streamlit deployment method')

df_pizza = pd.read_csv('https://raw.githubusercontent.com/tylerjrichards/Barstool_Pizza/master/pizza_data.csv')


sns.distplot(df_pizza['dave_score_int'])
plt.xlabel('Dave Score')
plt.ylabel('Proportion')
plt.title('Dave Pizza Score')
st.pyplot()