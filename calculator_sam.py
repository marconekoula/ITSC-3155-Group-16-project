#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cjeffcoa
"""

import math
import statistics


def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')

    if op in '^r%':
        a = float(input('Please type the first number: '))
        b = float(input('Please type the second number: '))

        if op == '^':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a**b)
        elif op == '%':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a%b)
        elif op == 'r':
            if (a < 0):
                return "Error: Cannot take the root of a negative number"
            else:
                return str(b) + 'th root of ' + str(a) + ' = ' + str(a**(1/b))
    elif op in '!sincostanln':
        a = float(input('Please type the number: '))

        if op == '!':
            return str(a)  + op + ' = ' + str(math.factorial(a))

        elif op == 'sin':
            return "sin(" + str(a) + ') = ' + str(math.sin(a))

        elif op == 'cos':
            return "cos(" + str(a) + ') = ' + str(math.cos(a))

        elif op == 'tan':
            return "tan(" + str(a) + ') = ' + str(math.tan(a))

        elif op == 'ln':
            return "ln(" + str(a) + ') = ' + str(math.log(a))

    else:
        return "Incorrect operator! Please select from the given options!"


def stats():
    listNum = int(input('How many numbers in your list?:'))
    nums =[]
    for i in range(listNum):
        nums.append(int(input("")))

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "mode, mean, gmean, hmean, median, range, stdev" : ')

    if op == 'mode':
        return statistics.multimode(nums)

    elif op == 'mean':
        return statistics.mean(nums)

    elif op == 'gmean':
        return statistics.geometric_mean(nums)

    elif op == 'hmean':
        return statistics.harmonic_mean(nums)

    elif op == 'median':
        return statistics.median(nums)

    elif op == 'stdev':
        return statistics.stdev(nums)

    elif op == 'range':
        return max(nums) - min(nums)




def main():  # Wrapper function

    print("""Choose a user
    1. Student
    2. Teacher
    3. Statistician""")
    choice = int(input('Please choose as 1, 2 or 3: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    elif choice == 3:
        print(stats())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()
