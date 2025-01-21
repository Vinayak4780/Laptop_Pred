import streamlit as st
import pickle 
import numpy as np
#pipe = pickle.load(open('pipe.pkl','rb'))
laptop_preds = pickle.load(open('laptop_preds.pkl','rb'))
st.title("Laptop Prediction")

#Brand
company = st.selectbox('Brand',laptop_preds['Company'].unique())

#Type of Laptop
type = st.selectbox('Type',laptop_preds['TypeName'].unique())

#Ram
Ram = st.selectbox('RAM(in GB)',[2,4,6,8,10,12,16,24,32,64])

#weight
weight = st.number_input('Weight of the Laptop')

#TouchScreen
Touchscreen = st.selectbox('Touchscreen',['No','Yes'])

#IPS
Ips = st.selectbox('IPS',['No','Yes'])

#ppi
Screen_size = st.number_input('Screen Size')

#resolution
Resolution = st.selectbox('Screen Resolution',['1920x1080','1336x768','1600x900','3840x2160','3200x1800','2800x1800','2560x1600','2560x1440','2304x1440'])

#CPU
Cpu = st.selectbox('Cpu',laptop_preds['Cpu Brand'].unique())

Hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048] )
Ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024] )
Gpu = st.selectbox('GPU', laptop_preds['Gpu_Brand'].unique())
Os = st.selectbox('OS', laptop_preds['os'].unique())
if st.button('Predict Price'):
   ppi = None
   if Touchscreen == 'Yes':
     Touchscreen=1
   else:
     Touchscreen= 0
   if Ips == 'Yes':
     Ips = 1
   else:
     Ips = 0
   x_res = int(Resolution.split('x')[0])
   y_res = int(Resolution.split('x')[1])
   ppi = ((x_res**2)+(y_res**2))**0.5/Screen_size
   query = np.array([company,type,Ram,weight,Touchscreen,Ips,ppi,Cpu,Hdd,Ssd,Gpu,Os])
   query = query.reshape(1,12)
   st.title(np.exp(pipe.predict(query)))
    
