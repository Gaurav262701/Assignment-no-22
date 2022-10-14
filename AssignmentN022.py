#!/usr/bin/env python
# coding: utf-8

# 
# # Assignment 22 Solutions

# 1.Create a function that takes three parameters where:
# x is the start of the range (inclusive).
# y is the end of the range (inclusive).
# n is the divisor to be checked against.

# In[1]:


def list_operation(start,end,divisor):
    out_list = []
    for i in range(start,end+1):
        if i%divisor == 0:
            out_list.append(i)
    print(f'output: --> {out_list}')
    
list_operation(1,10,3)
list_operation(7,9,2)
list_operation(15,20,7)
    


# 3.A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in a alphabetical order ? Create a function that takes in a list of names and returns the name of the secret society ?

# In[5]:


def society_name(in_list):
    out_string = []
    for i in in_list:
        out_string.append(i[0])
    output = ''.join(sorted(out_string))
    print(f'{in_list}-->{output}')

society_name(["Adam","Sarah","Malcolm"])
society_name(["Harry","newt","Luna","Cho"])
society_name(["Phoebe","Chandler","Rachel","Ross","Monica","joey"])
                         


# 4.An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

# In[7]:


def is_isogram(in_string):
    lower_in_string = in_string.lower()
    if len(lower_in_string) == len(set(lower_in_string)):
        print(f'{in_string}-->{True}')
    else:
        print(f'{in_string}-->{False}')
        
is_isogram("Algorism")
is_isogram("PasSword")
is_isogram("Consecutive")


# 5.Create a function that takes a string and returns True or False, depending on whether the characters are in order or not ?

# In[8]:


def is_in_order(in_string):
    in_string_sorted =''.join(sorted(in_string))
    if in_string == in_string_sorted:
        print(f'{in_string}-->{True}')
    else:
        print(f'{in_string}-->{False}')
        
is_in_order("abc")
is_in_order("edabit")
is_in_order("123")
is_in_order("xyzz")


# In[ ]:




