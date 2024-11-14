import streamlit as st
import pandas as pd
import time

st.title("통합데이터 서비스")
st.image('image.jpg')
data = pd.read_csv('tlftmq_members.csv')
data["PW"] = data["PW"].astype(str)

with st.form("login_form"):
    ID = st.text_input("ID",
                    placeholder="아이디를 입력하세요.")
    PW = st.text_input("password",
                    placeholder="비밀번호를 입력하세요.",
                    type="password")
    submit_button = st.form_submit_button("로그인")
    
if submit_button:
    if not ID or not PW:
        st.warning("ID와 비밀번호를 모두 입력해주세요.")
    else:
        user = data[(data["ID"]==ID)&(data["PW"]==PW)]
        if not user.empty:
            st.success(f"{ID}님 환영합니다!")
            st.session_state["ID"]=ID
            
            progress_text = "로그인 중입니다."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.switch_page("pages/tlftmq bike.py")
            
        else:
            st.warning('사용자 정보가 일치하지 않습니다.')
