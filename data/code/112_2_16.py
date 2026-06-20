from typing import Union

def add_numbers(num1: int, num2: int) -> int:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")
    return num1 + num2

if __name__ == '__main__':
    a = 10
    b = 5
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")
    
    x = -3
    y = 7
    result2 = add_numbers(x, y)
    print(f"The sum of {x} and {y} is {result2}")