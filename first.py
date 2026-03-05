import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="My Streamlit Site",
    page_icon="🚀",
    layout="wide"
)

# --- SIDEBAR ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Data Insights", "Contact"])

# --- HOME PAGE ---
if selection == "Home":
    st.title("Welcome to My Streamlit App 🌟")
    st.subheader("Building powerful web tools with pure Python.")
    
    st.markdown("""
    This website was built using **Streamlit**. No HTML or CSS required (unless you want to get fancy). 
    Use the sidebar to explore the different sections of the site!
    """)
    
    st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", caption="Coding made simple.")

# --- DATA SECTION ---
elif selection == "Data Insights":
    st.title("📊 Interactive Data Dashboard")
    st.write("Here is some randomly generated data visualized in real-time.")

    # Create dummy data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Product A', 'Product B', 'Product C']
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Raw Data")
        st.dataframe(chart_data)

    with col2:
        st.write("### Trend Analysis")
        st.line_chart(chart_data)

# --- CONTACT PAGE ---
elif selection == "Contact":
    st.title("📩 Get In Touch")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")
        
        if submit:
            st.success(f"Thanks {name}! Your message has been 'sent' (simulated).")