import streamlit as st
st.title('FIRST APP')
username = st.text_input('Username')
password = st.text_input('Password',type='password')
if st.button('Login'):
    if username == 'babisha' and password=='password':
        #st.write('Login Granted') 
        st.warning('Login Granted')    
    else:
       # st.write('Acces denied') 
        st.('Acces denied')    