#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [num for num in num_list if num % 2 == 0]
    return(num_list)
print(return_evens([1,2,3,4,5]))

def make_exclamation(sentence_list):
    sentence_list = [sentence + "!" for sentence in sentence_list if type(sentence) == str ]
    return(sentence_list)

print(make_exclamation(["Hello","I'm doing great","Python is fun"]))    