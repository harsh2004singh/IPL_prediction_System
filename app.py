from unittest import result

import streamlit as st
import pickle
import os
import traceback   # ⭐ add this

st.write("App started")  # to confirm app is running

model_path = os.path.join(os.path.dirname(__file__), "pipe.pkl")

try:
    pipe = pickle.load(open(model_path, "rb"))
    st.success("MODEL LOADED SUCCESSFULLY 🎉")

except Exception as e:
    st.error("MODEL FAILED TO LOAD ❌")
    st.text(traceback.format_exc())   # ⭐ this prints FULL error

import pandas as pd
teams = ['Royal Challengers Bangalore',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Gujarat Titans']
cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
        'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']
st.title('IPL Match System ')
col1, col2 = st.columns(2)
with col1:
   batting_team= st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team= st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select the host city',sorted(cities))
Target = st.number_input('Target')
col3, col4,col5 = st.columns(3)
with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets falls')
if st.button('Predict probablilty'):
    runs_left = Target - score
    balls_left =120 -(overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr= (runs_left*6)/balls_left


    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
                             'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[Target],
                             'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]
    st.text(batting_team + " - " + str(round(win*100)) + "%")
    st.text(bowling_team + " - " + str(round(loss*100)) + "%")






