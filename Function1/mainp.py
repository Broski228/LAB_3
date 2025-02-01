#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Conv(grams):
    ounces = 28.3495231 * grams
    return ounces



# In[4]:


def Temp(F):
    C = (5/9) * (F - 32)
    print("From Fahrenheit to Celsium :", C )



# In[7]:


def Puzzle(numheads, numlegs): #c + r = 35   2c + 4r = 94
    for cock in range (numheads + 1):
        rab = numheads - cock
        if(2 * cock + 4 * rab) == numlegs:
            return cock, rab

# In[15]:


def filter_prime(a):
    b = []
    for i in a:
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                b.append(i)
    return b



# In[23]:


import itertools

def print_permutations():
   
    user_input = input("Enter a string: ")
    
 
    permutations = itertools.permutations(user_input)
    

    for perm in permutations:
        print(''.join(perm))




# In[21]:


def reverse_words(sentence):

    words = sentence.split()
  
    reversed_words = ' '.join(reversed(words))
    return reversed_words


user_input = input("Enter a sentence: ")




# In[22]:


def has_33(nums):
    
    for i in range(len(nums) - 1): 
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False




# In[24]:


def spy_game(nums):
 
    target = [0, 0, 7]
   
    for num in nums:
        if num == target[0]:
            target.pop(0)  
        if not target:  
            return True
    return False





# In[1]:


import math
def V(r):
    return (4/3) * math.pi * (r**3) 




# In[26]:


def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:  
            unique_lst.append(item)
    return unique_lst





# In[29]:


def is_palindrome(s):
    
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_s == cleaned_s[::-1]




# In[31]:


def histogram(lst):
    for num in lst:
        print('*' * num)

    


# In[34]:


import random
def game():
    number = random.randint(1, 20)
    print("Hello! What is ur name?")
    a = input(" ")
    print("Well", a, "I am thinking of a number between 1 and 20.")
    att = 0
    
    while True:
        print("Take a guess")
        b = int(input(" "))
        att += 1
        if b < number :
            print("Your guess is too low.")
        elif b > number:
            print("Your guess is too hight.")
        else: 
            print(f"Good job {a} ! KBTU is proud of u, u get +20 social credits and lose all reatakes. U did in {att} attempts!")
            break



# In[ ]:




