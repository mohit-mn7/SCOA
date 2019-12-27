#!/usr/bin/env python
# coding: utf-8

# In[4]:


B1 = [1.0,0.15,0.3,0.5,0]


# In[5]:


B2 = [1,0.6,0.2,0.1,0]


# In[16]:


Union = []
for i in range(len(B1)):
    Union.append(max(B1[i],B2[i]))
    
print("Union Is: ",Union)


# In[3]:



Intersection = []
for i in range(len(B1)):
    Intersection.append(min(B1[i],B2[i]))
print("Intersection Is: ",Intersection)


# In[18]:


Compliment1 = []
for i in range(len(B1)):
    Compliment1.append(1-B1[i])
print("Compliment 1 Is: ",Compliment1)


# In[19]:


Compliment2 = []
for i in range(len(B1)):
    Compliment2.append(1-B2[i])
print("Compliment 2 Is: ",Compliment2)


# In[20]:


Difference1 = []
for i in range(len(B1)):
    Difference1.append(min(B1[i],Compliment2[i]))
print("Difference 1 Is: ",Difference1)


# In[15]:


Difference2 = []
for i in range(len(B1)):
    Difference2.append(min(B2[i],Compliment1[i]))
print("Difference2  Is: ",Difference2)


# In[25]:


#Cartesian Product - Method 1
print("Cartesian Product - Method 1")

for i in range(len(B1)):
    print()
    for j in range(len(B2)):
        print(min(B1[i],B2[j]), end = "   ")


# In[52]:

print()
#Cartesian Product - Method 2
print("Cartesian Product - Method 2")

rows = len(B1)
cols = len(B2)
CP = []
for i in range(rows):
    z = []
    CP.append(z)
for k in range(rows):
    for l in range(cols):
        CP[k].append(min(B1[k],B2[l]))
for rows in CP:
    print(rows)

#MatPlotLib

from matplotlib import pyplot as plt
x = [1,2,3,4,5]

plt.plot(x,B1,label="Set 1")
plt.plot(x,B2,label="Set 2")
plt.gca().legend(('Set-1','Set-2'))
plt.show()

plt.plot(x,Union)
plt.plot(x,Intersection)
plt.gca().legend(('Union','Intersection'))
plt.show()

rows = 2
cols = 2
R1 = []
for i in range(rows):
    z = []
    R1.append(z)
for k in range(rows):
    for l in range(cols):
        R1[k].append(int(input()))
for rows in R1:
    print(rows)



