# -*- coding: utf-8 -*-
"""Itransition_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NnFU4Hu9LcCQ2tyVKHw0c2jmxQwZX7Mg
"""



#Solution of Task-2
def sort_array(arr):
  ones = {}
  for i in arr:
    ones[i] = bin(i).count('1')

  return sorted(arr, key = lambda x : (ones[x], x))

print(sort_array([3,7,8,9]))