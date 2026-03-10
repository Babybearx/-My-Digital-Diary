import streamlit as st
import pandas as pd
from datetime import date

# Sidebar Navigation
st.sidebar.title("📓 My Digital Diary")
page = st.sidebar.radio("Navigate", ["Home", "Write Diary", "Diary Insights", "About"])

if page == "Home":
    st.title("📔 Hello Boss! Welcome to Your Digital Diary")

    st.header("Bible Verse of the Day : 1 Peter 5:7")
    st.write("*Give all your worries and cares to God, for he cares about you.*")

    st.image("https://images.unsplash.com/photo-1519681393784-d120267933ba")

    name = st.text_input("Enter your name")

    if name:
        st.success(f"Hey Wassup {name}! start writing your diary today!")

    st.subheader("Features")
    st.markdown("""
    - Write daily diary entries
    - Select your mood
    - Upload photos
    - Track your mood history
    - Save notes easily
    """)

    st.checkbox("I agree to keep my diary private")

    st.caption("*Your personal thoughts stay with you.*")

elif page == "Write Diary":

    st.title("✍ Write a New Diary Entry")

    entry_date = st.date_input("Select Date", date.today())

    title = st.text_input("Diary Title")

    mood = st.selectbox(
        "How are you feeling today?",
        ["😊 Happy", "😐 Neutral", "😢 Sad", "😡 Angry", "😴 Tired"]
    )

    diary_text = st.text_area("Write your diary entry here")

    uploaded_image = st.file_uploader("Upload a photo for today (optional)", type=["png","jpg","jpeg"])

    if uploaded_image:
        st.image(uploaded_image)

    importance = st.slider("Importance of today's entry", 1, 10, 5)

    save = st.button("Save Entry")

    if save:
        st.success("Your diary entry has been saved!")

    st.progress(50)

elif page == "Diary Insights":

    st.title("📊 Diary Insights")

    st.header("Mood Statistics")

    moods = ["Happy", "Neutral", "Sad", "Angry", "Tired"]
    mood_counts = [5,3,2,1,4]

    data = pd.DataFrame({
        "Mood": moods,
        "Count": mood_counts
    })

    st.dataframe(data)

    st.subheader("Mood Chart")
    st.bar_chart(data.set_index("Mood"))

    st.metric("Total Entries", "15")

    with st.expander("View Sample Diary Data"):
        st.write(data)

elif page == "About":

    st.title("About This App")

    st.header("What the App Does")
    st.write("""
    This digital diary application allows users to record daily thoughts, to give bible verse of the day,
    track moods, and store personal notes in an organized way.
    """)

    st.header("Target Users")
    st.write("""
    - Students
    - People who like journaling
    - Anyone who wants to record daily experiences
    """)

    st.header("Inputs and Outputs")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Inputs")
        st.markdown("""
        - Text input for diary entries
        - Mood selection
        - Image uploads
        - Date selection
        """)

    with col2:
        st.subheader("Outputs")
        st.markdown("""
        - Saved diary entries
        - Mood charts
        - Entry statistics
        """)


    st.info("This application was built using Streamlit.")
