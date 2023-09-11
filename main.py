import streamlit as st
import pandas
st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/Users/yashkumargupta/Desktop/Wallpapers/817Ihup5RnL.jpg")

with col2:
    st.title("Radhe Krishna With Flute")
    content = """
    राधा ने श्रीकृष्‍ण से और श्रीकृष्ण ने राधा से नि:स्वार्थ और आत्मिक प्रेम किया था। 
    इसी प्रेम का कारण आज श्रीकृष्ण के नाम के आगे राधा लगता है... राधे कृष्ण। 
    कोई रुक्मिणी कृष्ण क्यों नहीं कहता जबकि रुक्मिणी भी तो राधा की तरह प्रेम करती थीं।
    """

    message = """Below you can find some of the apps i have built in python. Feel free to contact me."""
    st.info(content)
    st.info(message)

col3, empty_col, col4 = st.columns(3)
df = pandas.read_csv("data.csv",sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")