import math
import streamlit as st
st.set_page_config(
    page_title="SQRT Curve",
)
st.header("Made By @Sid")
st.title("SQRT Curve Calculator")

score_input = st.text_input("Enter your score and total (e.g., 8/10)")

if score_input:
    try:
        score1, score2 = map(int, score_input.split("/"))
        percantagescore = (math.sqrt(score1) / math.sqrt(score2)) * 100
        st.success(f"Curved Score: {percantagescore:.2f}%")
    except:
        st.error("Invalid input. Use format 8/10.")
