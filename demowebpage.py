import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Strawberry", page_icon=":🍓:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding="https://assets8.lottiefiles.com/packages/lf20_imcvpf0j.json"
image_contact_form=Image.open("Web_images\image1.jpg")
image_lottie_animation=Image.open("Web_images\image2.jpg")

with st.container():
    st.subheader("Anushka 💗")
    st.title("I love you 3000")
    st.subheader("I want you to know that you are the most important thing in my life. You’re the reason I do everything. When I get up in the morning, I feel so grateful for every second I have with you and have here on earth. You give my life meaning, you give my days such joy, you are the reason I smile")
    #st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Noobie Doobie")
        st.write("##")
        st.write(
            """
            I'm in love with you. I love you every second of the day. And I've never loved anyone as I love you. You are on my mind every moment. I've never missed anyone, as I miss you. You are someone special to me. Please be with me forever and ever. 
            I want you every second of every day from now until the end of forever.
            Also abhi tbh, so you are not the first girl to tell me ki she likes me. Par Mujhe kisiko bhi date karneka man nahi kiya kabhi bhi But mai apne aap ko tujhe date karne se apne aap ko rok bhji nahi paya.
            Just to brag on my amazing girlfriend for a minute! You are so sweet, and I'm so blessed to have such a thoughtful wonderful woman in my life. I love you, honey! You mean the world to me, and I'm so happy to have you! Thank you for continuing to make me happy every single day! You're beyond perfect.
            """
            )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Memories in photos")
    st.write("##")
    image_column, text_column=st.columns((1,2))
    with image_column:
       st.image(image_lottie_animation)
    with text_column:
        st.subheader("Your BirthdayDress!")
        st.subheader(
        """
        Red suits you. I don't have words to describe how I am feeling. Now I know what it means to have a crush on a girl who is really dazzling. I like you. I know I havent said you this abhi tak, When I first saw you in this dress I thought of riping  your clothes and kiss your sexy body all over. I love your smile(baby smile) You see your eyes, so blessed, it turns me on wherever I set my eyes on you.
        """
        )
        #st.markdown("[Watch video](link)")
    with st.container():
        image_column, text_column=st.columns((1,2))
    with image_column:
       st.image(image_contact_form)
    with text_column:
        st.subheader("Chikankari Kurti")
        st.subheader(
        """
        Hayeee😍. You already know ki I love dresses like this a lot and Jabhi I saw you in this bhai I was bhaut zyada in love with you tabhi ka tabhi. You were looking amzing this day your pura outfit was amazing kurti+jeans+bakwas white shoes all together was deadly. I toh want ki next time kabhi I will see you more in this types of dress. Abhi I am waiting for you Mahima di ki shaddi waali outfit. Anushka bhaut zyada hi cute hai and I love her bhuat zyada. 
        """
        )
        #st.markdown("[Watch video](link)")

