#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_list = []  
    for num in int_list:  
        squared_list.append(num ** 2)  
    return squared_list  

def fizzbuzz():
    for num in range(1, 101):  # This Loop through numbers from 1 to 100
        if num % 3 == 0 and num % 5 == 0:  # This will Check if the number is divisible by both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")
        elif num % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")
        else:  # If none of the above conditions are met, simply print the number
            print(num)


