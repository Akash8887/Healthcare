import streamlit as st
# from streamlit_star_rating import st_star_rating

def star_rating(label, default_value=0, max_stars=5):
    st.write(label)
    selected_stars = st.slider("", 0, max_stars, default_value, 1)
    return selected_stars

st.title("Contact Us 📫")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.text_input("Name")
st.text_input("Mobile number", placeholder="+91 XXXXX XXXXX")
st.radio("Select Gender", ["Male", "Female"], index=None)
st.text_input("Your email", placeholder="@gami.com")
st.text_area("Your message")

# st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = None, key = "rating", emoticons = True )

feedback_rating = star_rating("Rate this feature:", default_value=3)

st.write("You rated this feature:", feedback_rating, "stars")

st.button("Submit")