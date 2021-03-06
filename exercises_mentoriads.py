# -*- coding: utf-8 -*-
"""Exercises_MentoriaDS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6urEl95Vb5DsbnNSvJH2E1zcOW8YQwi

Exercise 08-10-2021
"""

people = {
    'Luiz'      : 'laranja',
    'Leonardo'  : 'vermelho',
    'Morgana'   : 'rosa'
}

def createPerson(name, color): 
  if name in people:
    print("The user already exists.")
  else:
    people[name] = color
    print("Color added.")

def updateColor(name, color):
  if name in people:
    people.update({name : color})
    print("Color updated.")
  else:
    print("The user doesn't exists.")
    
createPerson('Greg', 'Azul')
updateColor('Morgana', 'Azul')

print(people)

"""Exercise 08-17-2021"""

import pandas as pd
df = pd.read_csv("Sales.csv")
print(df)

#Total amount sold 
df['quantity'].sum()

#Total amount by each year
df.groupby("year").sum()['quantity']
df.groupby('year')['quantity'].sum()

#The person that bought most
df["person"].max()

#The person that bought less 
df["person"].min()

#Total sales by gender
# ????

#Most sold product in general 
print(df.groupby("product_id").max())

#Most sold product by year