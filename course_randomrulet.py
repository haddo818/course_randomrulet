import streamlit as st
import random 
import time

#기본 세팅 설정
st.set_page_config(
   page_title="랜덤룰렛",
   page_icon="🤑",
   layout="centered",
   initial_sidebar_state="expanded",
) #성공함. 

#text칸 초기화하는 함수 설정.
def clear_text():
    st.session_state["text"] = ""

#본 코드
st.title("밥을 어디에서 먹으면 좋을까요? 랜덤 룰렛 ദി(⩌ᴗ⩌ )")
candidate = st.number_input("후보군의 개수를 지정해주세요!" +"( ´ ▽ ` )ﾉ", min_value = 1, step = 1)
date = st.text_input("언제 식사하나요?(￣∠ ￣ )ﾉ", placeholder = "예: 내일 저녁") 
res = [] #restaurant의 약자. 식당들을 입력받을 비어있는 리스트. 
for i in range(int(candidate)):
  restaurant = st.text_input(f"{i+1}번째! 가고 싶은 식당(or메뉴)을 입력하세요!", key=f"restaurant_{i}")
  if restaurant:
    res.append(restaurant)

#랜덤룰렛을 돌리는 버튼 
if st.button("랜덤룰렛돌리기(*´∀｀*)ﾉ｡+ﾟ *｡"):
  if res:
    st.write(f"우리가 **{date}** 에 갈 식당은...? 두구두구두구두구둑...")
    #양쪽에 **을 붙이면 자연스럽게 text가 bold처리가 되어야 하는데 안 된다, 어쩌지? 
    time.sleep(2)
    st.write(f"**{random.choice(res)}** 입니다!") #양쪽에 **을 붙이면 자연스럽게 text가 bold처리가 된다. 
  else:
    st.write("추천할 식당을 입력해주세요.")

#리셋하는 버튼 
#후보1.처음 상태를 그대로 저장했다가, "다시 하기" 버튼을 눌렀을 때, 저장된 값을 불러와서 채워넣는다던가? 
#후보2.아예 텍스트 박스를 비워버린다거나? 
#후보3.버튼을 누르면 새로고침을 하게 한다거나? --> 이걸로 가보자.
from streamlit_js_eval import streamlit_js_eval
    
if st.button("마음에 안 든다 다시 돌려라"):
  streamlit_js_eval(js_expressions="parent.window.location.reload()")
  #st.experimental_rerun()  --> 실행이 잘 안된다. 버전 상의 문제인 것 같다. 안 쓰는 게 좋을 것 같긴 하다.
  #st.rerun() --> st.experimental_rerun() 대신 쓸 수 있는 것으로 안내 받았지만, 후보3은 rerun을 목표로 하는 것이 아니라 완전한 페이지 새로고침을 목표로 하기 때문에 적절하지 않은 것 같다.
  #reset_state() --> 기타 방법을 강구하다가 시도해본방법, 함수를 활용하는 방법이다. 아닌 것같다.
  #candidate = candidate.delete #아래는 .delete를 해보면 혹시 입력되었던 값이 사라지지는 않을까 싶어서 시도해본 것이다.
  #date = date.delete
  #res = []
  #restaurant = retaurant.delete
  #실패함. 다른 방법 찾기.


#streamlit run /workspaces/randomrulet/randomruletst.py
