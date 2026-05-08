import numpy as np
def AND(a, b):
    return a & b
def OR(a, b):
    return a | b
def NOT(a):
    return 1 - a
if __name__ == '__main__':
    print("--- AND Gate Demonstration ---")
    a_and = 0
    b_and = 0
    print(f"AND(0, 0) = {AND(a_and, b_and)}")
    a_and = 0
    b_and = 1
    print(f"AND(0, 1) = {AND(a_and, b_and)}")
    a_and = 1
    b_and = 0
    print(f"AND(1, 0) = {AND(a_and, b_and)}")
    a_and = 1
    b_and = 1
    print(f"AND(1, 1) = {AND(a_and, b_and)}")
    print("\n--- OR Gate Demonstration ---")
    a_or = 0
    b_or = 0
    print(f"OR(0, 0) = {OR(a_or, b_or)}")
    a_or = 0
    b_or = 1
    print(f"OR(0, 1) = {OR(a_or, b_or)}")
    a_or = 1
    b_or = 0
    print(f"OR(1, 0) = {OR(a_or, b_or)}")
    a_or = 1
    b_or = 1
    print(f"OR(1, 1) = {OR(a_or, b_or)}")
    print("\n--- NOT Gate Demonstration ---")
    a_not = 0
    print(f"NOT(0) = {NOT(a_not)}")
    a_not = 1
    print(f"NOT(1) = {NOT(a_not)}")