from typing import Union

def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

if __name__ == '__main__':
    a = 10
    b = 5
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")