import streamlit as st
st.title('a small program')
st.subheader('I am Suu Wai Moe')
st.write('My first streamlit app')
st.write('You have to enter your scores for each subject.')
Myanmar_score = st.Myanmar_score_input('Enter Myanmar Score:')
English_score= st.English_score_input('Enter English score:')
Maths_score = st.Maths_score_input('Enter Maths Score:')
Chemistry_score = st.Chemistry_score_input('Enter Chemistry Score:')
Physics_score = st.Physics_score_input('Enter Physics Score:')
Bio_score = st.Bio_score_input('Enter Bio Score:')
if Myanmar_score >= 40 and English_score>= 40 and Maths_score >= 40 and Chemistry_score >= 40 and Physics_score >= 40 and Bio_score >= 40:
    st.write("You've passed the exam")
    if Myanmar_score >= 75:
        st.write('Myanmar Distinction')
    if English_score >= 75:
        st.write('English Distinction')
    if Maths_score >= 80:
        st.write('Maths Distinction')
    if Chemistry_score >= 80:
        st.write('Chemistry Distinction')
    if Physics_score >= 80:
        st.write('Physics Distinction')
    if Bio_score >= 75:
        st.write('Bio Distinction')
else:
    st.write("You fail the exam")
Total_Score=Myanmar_score+English_score+Maths_score+Chemistry_score+Physics_score+Bio_score
st.write('Your total score:',Total_Score)
