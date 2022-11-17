# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_min(arr):
    # This function is going to find the min value of the input array and return it.
    c = 0
    for b in arr:
        if b < c:
            c = b
    return c


def division(a, b):
    # This function is going to get the quotient of division and return it.
    sleep(2)
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    return "Cannot divide by zero."


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = [1, 2, 3, 4]
    d = find_min(a)
    print(d)
    print(division(4, 0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
