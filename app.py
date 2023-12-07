from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local Css

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/ccd351fa-6625-4172-9082-8133922133d6/V9YuUtgXl2.json")
lottie_email = load_lottieurl("https://lottie.host/cf262121-a926-4935-b875-de2f0c5e1443/egpAV4JoPj.json")
img_project1 = Image.open("image/Lykan.jpg")
img_project2 = Image.open("images/relaxing.jpg")

# --- Side Bar Section ---
with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Project' ,'About', 'Feedback'], 
                             iconName=['home', 'link', 'info', 'mail'],
                             styles = {'navtab': {'background-color':'#1e7aea',
                                                  'color': '#fcfcfc',
                                                  'font-size': '18px',
                                                  'transition': '1s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'
                                                  },
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}
                                                          },
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'
                                                   },
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'
                                                    }
                                        },
                             key="1" ,default_choice=0)

# --- Home Section ---
if tabs =='Home':
    with st.container():
        column_left, column_right = st.columns((2,1))
        with column_left:
            st.write("---")
            st.title("This is my webpage")
            st.subheader("Hi :wave:, I am Sean Earl R. Escatron")
            st.write("I am a Computer Engineering student from SNSU")
            st.write("learn more by watching tutorial youtube.")
            st.write("click the link below and it will show you my creation.")
            st.write("[Github Link Here](https://github.com/seanearl2003/MyWebpage/settings)")
        with column_right:
            pass

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("My Project")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            # insert image
            st.image(img_project1)
        with text_column:
            st.subheader("Lykan")
            st.write(
                """ 
                This is a hypercar with a unique showing its featrue which made in Html, Css and Java Script. 
                """
                """ 
                This web app will serve as my project. 
                """
                """
                This is a sample of a webpage i create. 
                """
                """"""
            )
            st.markdown("[Github Link](https://github.com/seanearl2003/MyWebpage/settings)")
    with st.container():
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_project2) # insert image
        with text_column:
            st.subheader("How to add a contact form in your Streamit App")
            st.write(
                """
                Want to add a contact form to your streamlit website.
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service 'Form Submit'.
                """
            )
            st.markdown("[Watch Here](https://youtu.be/FOULV9Xij_8)")

# --- About Section ---
elif tabs == 'About':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("""
                I am a computer engineering student in Surigao del Norte State University.
                - I am currently studying Python, Java, Html and Css.
                - All of my projects will success.
                - My project is finally finish.
            """)
            st.write("For the meantime you can watch this youtube video to learn more about how to make a webpage!")
            st.write("[Youtube](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st_lottie(lottie_coding, height=500, key="coding")

# --- Feedback form Section ---
elif tabs == 'Feedback':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Get in touch with me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/seanearlescatron7@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_email, height=200, key="email")
