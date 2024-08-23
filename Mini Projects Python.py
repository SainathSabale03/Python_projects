#!/usr/bin/env python
# coding: utf-8

# In[1]:


game_list=[0,1,2]


# In[2]:


def display_game(game_list):
    print("Here is the current list:")
    print(game_list)


# In[3]:


display_game(game_list)


# In[4]:


def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice!")
        
    return int(choice)


# In[5]:


position_choice()


# In[6]:


def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list



# In[7]:


replacement_choice(game_list,2)


# In[8]:


def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input("Keep Playing ? (Y or N): ")
        
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N")
     
    if choice == "Y":
        return True
    else:
        return False
    


# In[9]:


gameon_choice()


# In[10]:


game_on = True 
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    
    


# In[ ]:




