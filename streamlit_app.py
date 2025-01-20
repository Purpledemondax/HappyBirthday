import streamlit as st
import time
import numpy as np
import pandas as pd

_LOREM_IPSUM = """
    **Happy Birthday Dad**,  I'm wishing you a very happy birthday. You have been a great
    inspiration to me both in your intelligence and drive. I'm very proud to call you my father and have always been.
"""

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.08)

    

name = "Dad"
# Title of the app
st.title("🎉 Happy Birthday Dad 🎂")

progress_text = "Loading your celebration"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()



# Display a button to wish Happy Birthday
if st.button("Celebrate 🎉"):
    if name:
        st.balloons()
        st.success(f"🎉🎂 Happy Birthday, {name}! 🎂🎉")
        st.write(
            "Wishing you a fantastic day filled with love, laughter, and all your favorite things! - From your favourite child 🥳🎁"
        )
        time.sleep(2.5)
        st.write_stream(stream_data)
        


st.button("Love You")