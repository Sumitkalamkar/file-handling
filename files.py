import streamlit as st
import pandas as pd
st.subheader('loading the csv file')

df=st.file_uploader("upload the csv file"   ,type=['csv','xlsx'])

if df is not None:
    ls=pd.read_csv(df)
    st.table(ls)

st.subheader('Dealing With image')
img_file=st.file_uploader("upload the image",type=['jpeg','png'])
if img_file is not None:
    st.image(img_file)

st.subheader("working with the vidio file")
video_file=st.file_uploader("upload the vidio",type=['mkv','mp4'])
if video_file is not None:
    st.video(video_file,start_time=0)

st.subheader("working with the audio file")
audio_file=st.file_uploader("upload the audio",type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())
