from typing import Union

def add_numbers(num1: int, num2: int) -> int:
    if not all(isinstance(n, (int)) for n in [num1, num2]):
        raise ValueError("Both inputs must be integers")
    return num1 + num2

if __name__ == '__main__':
    a = 10
    b = 5
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")