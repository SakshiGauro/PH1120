#!/usr/bin/env python
# coding: utf-8

# In[1]:


#===========================================================
# WPI PHYSICS DEPARTMENT - 2020-2021
# PH1120/21 Lab 3 - Capacitance
# Sample code for calculating capacitance and uncertainties
#-----------------------------------------------------------
# Copyright Amelia Nishimura 2020 :v
#-----------------------------------------------------------
##--------------------
##lab4 Resistors

#Parameter C from Logger Pro is re-defined as 'CPar' below
Cpar1 = 0.0511  #find from Logger Pro fit, value 'C'

cpar1_uncertainty = 0.00002236 #Get from +/- fit from loggerPro

R = 49.511 # Use resistor value from circuit 
r_uncertainty = R*.2 #Use the tolerance band on your 22k Ohm resistor. 
#A resistor band guide can be found on the back of your board

c1 = 1/(R * Cpar1) #Eq 1


# In[2]:


#Equation 2 Function
def MultError(dx, x, dy, y, A):
    ii = (dx / abs(x) ) + (dy / abs(y))
    dA = A * ii
    return dA


# In[3]:


#This is where we run through Eq 2
c1_uncertainty = MultError(cpar1_uncertainty, Cpar1, r_uncertainty, R,c1)

print(f'Eq 1 & 2: Measured (on LoggerPro) resistor: {c1} +/- {c1_uncertainty} F')


# In[ ]:





# In[ ]:





# In[ ]:




