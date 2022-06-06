#!/usr/bin/env python3

import random
import time
import math
import operator

# SETUP

delay = 1 # <-- wait between new operations

# clear console
clear_console = True # <-- if want to clear console
limit_chars = 10 # <-- clear console after X operations


count = 0 # <-- count operations


ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
}

count_correct = 0
count_incorrect = 0
count_skipped = 0

true = "Correct"
false = "Incorrect"
Help = """
Try to type the correct number.

To skip, just press ENTER

To stop, press CTRL + C
"""

def clear():
    import platform
    import os
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

# if you get to much numbers after a dot
# you can truncate it until it'll have 3 numbers after a dot
def truncate(num, dig):
    stepper = 10.0 ** dig
    return math.trunc(stepper *num) / stepper

def main():
    global count
    global limit_chars
    global clear_console
    global count_correct
    global count_incorrect
    global count_skipped

    print(Help)

    while 1:
        try:

            num1 = random.randint(1,150)

            op = random.choice(list(ops.keys()))

            if op == "/": num2 = random.randint(2,10)
            elif op == "*": num2 = random.randint(2,20)
            else: num2 = random.randint(1,150)

            answer = ops.get(op)(num1,num2)

            opp = f"{num1} {op} {num2} ="

            user_try = input(str(opp) + ' ')

            if user_try == '':
                print('Answer: ' + str(answer)+ '\n')
                count_skipped += 1
            elif float(user_try) == answer or float(user_try) == truncate(answer,3):
                print(true + '\n')
                count_correct += 1
            
            else:
                print(false + ', Correct answer: ' + str(answer)+ '\n')
                count_incorrect += 1

            time.sleep(delay)

            count += 1
            if clear_console and count == limit_chars:
                count = 0
                clear()

        except KeyboardInterrupt:
            total = count_correct+count_incorrect+count_skipped
            if clear_console: clear()

            print("""
Correct answers: {}/{}

Incorrect answers: {}/{}

Skipped: {}/{}

""".format(count_correct,total,count_incorrect,total,count_skipped,total))
            exit(0)

        except ValueError:
            print("Oh, please type numbers only!!")
            exit(1)

if __name__ == '__main__':
    main()
