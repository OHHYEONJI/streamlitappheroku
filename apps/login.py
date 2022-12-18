# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:07:35 2022

@author: Hyeonji Oh
"""

# import libraries needed
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle
import lifelines

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# loading navigation bar style
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# create navigation bar
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #153888;">
  <a class="navbar-brand" href="#" target="_blank">LASF prediction model</a>
""", unsafe_allow_html=True)


def app():
    st.title('Log in for access')
    username = st.text_input('User ID')
    password = st.text_input('Password')
    if st.button('login'):
        if password == '12345':
            st.success('logged In as {}'.format(username))
        else:
            st.warning('Incorrect Username/Password')