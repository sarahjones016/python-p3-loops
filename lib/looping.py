#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print(f"Happy New Year!")


def square_integers(int_list):
    int_squared = [num * num for num in int_list]
    return(int_squared)

def fizzbuzz():
    i = 0
    while i < 100:
        i += 1
        if (i % 3 == 0 and i % 5 == 0):
            print(f"FizzBuzz")
        elif (i % 3 == 0):
            print(f"Fizz")
        elif (i % 5 == 0):
            print(f"Buzz")
        else:
            print(f"{i}")