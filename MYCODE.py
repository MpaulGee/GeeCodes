#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t


# In[5]:


t.bgcolor("Black")
t.pensize(5)
t.speed(1)
t.color("red")
t.begin_fill()
t.left(150)
t.forward(180)
t.fillcolor("red")
t.circle(-90, 180)
t.setheading(60)
t.circle(-90, 180)
t.forward(180)
t.end_fill()
t.hideturtle()
msg = "MY LOVE"
t.write(msg, move=True,align="left" ,
        font=("Arial", 25, "italic", "bold"))


# In[ ]:




