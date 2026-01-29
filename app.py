import streamlit as st

#header
st.header("WELCOME TO ANURAG UNIVERSITY I-BLOCK")

#Title of the app
st.title("welcome to student details")

#sub header of the app
st.subheader("MANAGE STUDENT RECORDS EFIICIENTLY AND EFFFECTIVELY")

#text
st.text("HEY HEYYY")
st.markdown("----------")
st.text("this application used for performance of crud application")

#write method to provide additional details
st.write("HERO")
st.write(123)
st.markdown("### SRIRAM:")
st.markdown("*italic text*")

st.markdown("<h3 style = 'color:red'>RED TEXT</h3>",unsafe_allow_html=True)   
#code method to display code snippets
st.code("""
     def add(a,b):
        return a + body
        """,language="python")
#st.latex
st.latex(r'''
a^2 + b^2 =c^2
         ''')
#divider method to seperate sections
st.divider()
st.caption("LET'S GO ORANGE ARMY")

           
#st button
if st.button("click me"):
    st.write("HEY EVERYONE")
    st.success("operations successfull!")
    st.snow()
else:
    st.write("button not clicked yet")
    st.error("connection error")
#TEXT INPUT
name=st.text_input("enter your name:")
if name:
    st.write(f"Hello,{name}!") 
else:
  
  st.error("invalid input")
  #number_input
  #st.text_area
  feedback=st.text_area("HELLO")
  st.write("feedback")
  if st.checkbox("i agree to the terms and conditions"):
      st.write("thank yu for agreeing")
      #RADIO BUTTON   
      country = st.selectbox("select your country:",("india","usa","dubai"))
st.write(f"you selected:{country}")
skills = st.multiselect(
   "select skills",
   ["python","sql"]
)
st.write("Skills:",skills)
age = st.slider("select your age:",1,2,3)
st.write(f"you are {age} years old.")
#file uploader
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")

#form method
with st.form("my_form"):
   name = st.text_input("name")
   age = st.number_input("age",1,90)
   submit = st.form_submit_button("submit")
if submit:
   st.write(name,age)

#form submit button method
with st.form("login"):
   user = st.text_input("user")
   pwd = st.text_input("pwd",type="password")
   login = st.form_submit_button("login")
if login:
   st.success("login successfull")
   st.divider()

#columns method
col1,col2,col3=st.columns(3)
with col1:
   st.header("colum 1")
   st.write("this is column")
   st.divider()
with col2:
   st.header("colum 2")
   st.write("this is column 2")
   st.divider()
with col3:
   st.header("colum 3")
   st.write("this is column 3")
   st.divider()

#table method
data = {
    'Name': ['Hari', 'harsh', 'Ram'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
#sider bar

st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

@st.cache_data
def load_data():
   return [1, 2, 3, 4]

data= load_data()
st.write(data)
   