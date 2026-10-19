import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title('App name')
def f(x):
    return x**3+4*x**2+x-1
def df(x):
    return 3*x**2+8*x+1
#main
err=1000
x=st.sidebar.number_input('Enter a initial condition')
plt.plot(x,f(x),'ko')
k=0
while(err>=0.0001):
    k=k+1
    xnp1 = x - f(x)/df(x)
    err = abs(xnp1-x)
    x = xnp1
    plt.plot(x,f(x),'y*')
st.write('Root is',xnp1)
st.write('No. of iteration',k)
xi = np.linspace(-5,5,100)
#yi = 
plt.plot(xi,f(xi))
plt.plot(xnp1,f(xnp1),'ro')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y=f(x)')
st.pyplot(plt)
