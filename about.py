import streamlit as st


def main():
    st.markdown("<h3 style='color:blue;font-weight:bold;'><u>About</h3>", unsafe_allow_html=True)
    st.subheader('CODE FOR A BRIGHTER TOMORROW')

    st.write('IBM Hack Challenge 2020 is all about _coding for a cause_. It’s about finding solutions to problems '
             'plaguing society today. It is an opportunity to showcase your coding talent, learn new technologies and '
             'build an efficiently working solution.')

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:red;font-weight:bold;'><u>Our problem statement</h3>", unsafe_allow_html=True)
    st.subheader('Sentiment Analysis of COVID-19 Tweets Visualization Dashboard')

    st.write('''The sentiment analysis of Indians after the extension of lockdown announcements to be analyzed with the relevant #tags on twitter and build a predictive analytics model to understand the behavior of people if the lockdown is further extended.
Also develop a dashboard with visualization of people reaction to the govt announcements on lockdown extension ''')


if __name__ == '__main__':
    main()
