#!/usr/bin/env python3


def return_evens(num_list):
       
    return [n for n in num_list if n%2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = return_evens(numbers)
print(even_numbers)

def make_exclamation(sentence_list):
    # return list with exclamation marks
      return [sentence + "!" for sentence in sentence_list]
sentence_list = ["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentence_list))