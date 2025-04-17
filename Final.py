import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('SpendWise Expense :violet[Tracker] :🥰:')
st.markdown(
    """
    <style>
        .stApp {
            background-color:black;
            color: white; 
        }

        section[data-testid="stSidebar"] {
            background-color: #151a37;
              color: white;
        }
        div.stButton > button {
        background-color: #4CAF50;  /* Green */
        color: white;
        padding: 0.5em 1em;
        font-size: 16px;
        border: none;
        border-radius: 8px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #45a049;
        color: white;
        transform: scale(1.05);
    }
        
       
    </style>
    """,
    unsafe_allow_html=True
)

if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date','Category', 'Amount', 'Description'])

def add_expense(date,category,amount,description):
    new_expense = pd.DataFrame([[date, category,amount,description]], columns=st.session_state.expenses.columns)
    
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)


def save_expenses():
    st.session_state.expenses.to_csv('expense.csv', index=False)
    st.success("Expenses Saved Successfully!")

def load_expenses():
    st.session_state.expenses = pd.read_csv('expense.csv')
    st.success("Expenses loaded Successfully!")

def visualize_expenses():
    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.barplot(data=st.session_state.expenses, x='Category', y='Amount', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.warning("No expense to Visualize!")
    
    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.lineplot(data=st.session_state.expenses, x='Category', y='Amount', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.warning("No expense to Visualize!")
    

    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.boxplot(data=st.session_state.expenses, x='Category', y='Amount', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.warning("No expense to Visualize!")


    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.scatterplot(data=st.session_state.expenses, x='Category', y='Amount', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.warning("No expense to Visualize!")
    




with st.sidebar:
    st.subheader('Add Expense')
    date = st.date_input("Date")
    category = st.selectbox("Category", ['Food', 'Transport', 'Entertainment', 'Utilities', 'Others'])
    amount= st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_input("Description")

    if st.button('Add'):
        add_expense(date,category,amount,description)
        st.success("Expense Added!")

    
st.header('File Operations')
if st.button('Save Expensses'):
        save_expenses()
        
if st.button('Load Expenses'):
        load_expenses()

st.header('Expenses')
st.write(st.session_state.expenses)

st.header('Visualization')
if st.button('Visualize Expenses'):
        visualize_expenses()
