#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("SIP Calculator")
print()
user=input("SIP Investment or Lumpsum: ")
def SIP():
    amount=int(input("Total investment: "))
    time=int(input("Investment period(in years)"))
    returns=int(input("Returns from 0.0% to 50%:"))
    
    r=returns/(12*100)
    n=time*12
    sip_fv=amount*(((1+r)**n-1)/r)*(1+r)
    rsipamount=round(sip_fv,2)
    print(rsipamount)
    
def Lumpsum():
    amount=int(input("Total investment: "))
    time=int(input("Investment period(in years)"))
    returns=int(input("Returns from 0.0% to 50%:"))
    r=returns/100
    n=time*12
    lumpsum=amount*(1+r)**n
    rlumpsum=round(lumpsum,2)
    print(rlumpsum)

if user=="SIP":
    SIP()
elif user=="Lumpsum":
    Lumpsum()
else:
    print("ERROR 404")


# In[ ]:




