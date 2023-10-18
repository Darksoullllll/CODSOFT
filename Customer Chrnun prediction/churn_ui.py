import streamlit as st
import skops.io as sco
st.title("CUSTOMER CHRUN PREDCITION")

cname =  st.text_input("Customer Name: ")

ccredit =st.number_input("Your Credit Score: ")

loc = ['France','Spain','Germany']
cloc = st.selectbox("Select Your Location",loc)

gender=['Male', 'Female' ]
cgender = st.selectbox("Gender",gender)

cage = st.number_input("Enter Your Age: ")
#Tenure,CurrentBalance,Noofproduct,has credit card,is active meme,salary
ctenure=st.number_input("Enter Your Tenure: ")

cbal = st.number_input("Your Current Balance: ")

nprod = st.number_input("Number of Products Purchased: ",min_value=0 ,max_value=15)

ccreditcard = st.selectbox("Do You have Credit Card: ",['Yes','No'])

cactive =st.selectbox("Your a Active member or not: ",['Yes','No'])

csalary = st.number_input("Your Salary")

bt =st.button("Submit")

ccredit_dict = {
    "Yes": 1,
    "No":0
}
cactive_dict = {
    "Yes":1,
    "No":0
}

if(bt):
    model = sco.load("Chrun_Model")
    if(cloc == 'France' and cgender == 'Male'):
        res1 = model.predict([[1,0,0,0,1,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        if(res1[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")
    if(cloc == 'France' and cgender == 'Female'):
        res2 = model.predict([[1,0,0,1,0,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        if(res2[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")


    if(cloc == 'Spain' and cgender == 'Male'):
        res3 = model.predict([[0,0,1,0,1,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        if(res3[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")
    if(cloc == 'Spain' and cgender == 'Female'):
        res4 = model.predict([[0,0,1,1,0,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        if(res4[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")

    if(cloc == 'Germany' and cgender == 'Male'):
        res5 = model.predict([[0,1,0,0,1,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        print(res5)
        if(res5[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")
    if(cloc == 'Germany' and cgender == 'Female'):
        res6 = model.predict([[0,1,0,1,0,int(ccredit),int(cage),int(ctenure),int(cbal),int(nprod),ccredit_dict[ccreditcard],cactive_dict[cactive],int(csalary)]])
        if(res6[0] == 0):
            st.write(cname + " Not Going To left The Bank")
        else:
            st.write(cname + " Going To left The Bank")