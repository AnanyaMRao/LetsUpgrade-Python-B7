#!/usr/bin/env python
# coding: utf-8

# Question 1: 
# You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
# 1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
# the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
# later”

# In[7]:


altitude=input("Altitude: ")
if int(altitude)<=1000:
    print("Safe to Land")
elif int(altitude) in range(1001,5000):
    print("Bring down to 1000")
else:
    print("Turn Around")


# Question 2: 
# Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
# function.
# 

# In[18]:


prime_numbers=[]
for num in range(1,201):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
                prime_numbers.append(num)
print("these are the prime numbers: ",prime_numbers)


# In[ ]:





# In[ ]:




