# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:29:58 2022

@author: chaima
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:\\Users\\chaima\\Desktop\ProjetML\\trained_modelheart.sav', 'rb'))







#creating a function for prediction

def heartAttackPrediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return('The person has less chance of having a heart attack')
    else:
      return('The person has more chance of having a heart attack')


def main():
    
    #giving a title
    st.title('Heart Attack Prediction')
    
    #getting the input data from the user 
    
    #age
    age = st.text_input('Age of the patient', key="1")
    #sex
    sex = st.selectbox('Sex of the patient',{'Male','Female'} , index=0)
    
    if sex == 'Male' :
        sex = 0 
    else :
        sex = 1 
    
    
    #cp
    cp = st.selectbox('Chest Pain type ',{'typical angina:0','atypical angina:1 ','non-anginal pain:2', 'asymptomatic : 3'} , index=0)
    
    if cp == 'typical angina' :
        cp = 0 
    elif cp == 'atypical angina' :
        cp = 1 
    elif cp == 'non-anginal pain' :
        cp = 2
    else :
        cp = 3
        
#trtbps
    trtbps = st.text_input('Resting blood pressure (in mm Hg)', key="4")
    #chol
    chol = st.text_input('Cholestoral in mg/dl fetched via BMI sensor', key="5")
    #fbs
    fbs = st.radio("Fasting blood sugar > 120 mg/dl",('True','false'))
    
    if fbs == 'True' :
        fbs= 1 
    else :
        fbs = 0
    
    #restecg
    restecg = st.text_input('Resting electrocardiographic results', key="7")
    thalachh = st.text_input('Maximum heart rate achieved', key="8")
    
  
    exng = st.radio("Exercise induced angina",('No', 'Yes'))
    if exng == 'No':
        exng = 0
    else:
        exng = 1
        
        
    
    
    oldpeak = st.text_input('Previous peak', key="10")
    slp = st.text_input('Speech-language pathologist', key="11")
    caa = st.text_input('Number of major vessels (0-3)', key="12")
    thall = st.text_input('Thallium (0-3) ', key="13") 
    
    #code for prediction 
    diagnosis = ''
     
    if st.button('Heart Attack Test Result'):
        diagnosis = heartAttackPrediction([age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall])
    
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
        main()

    
    
    
    
    
    