from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Union[int, float]:
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

if __name__ == '__main__':
    num1 = 25
    num2 = 4
    print(f"The first number is: {num1}")
    print(f"The second number is: {num2}")
    print(f"The sum of the two numbers is: {add(num1, num2)}")
    print(f"The difference between the two numbers is: {subtract(num1, num2)}")
    print(f"The product of the two numbers is: {multiply(num1, num2)}")
    try:
        print(f"The result of division is: {divide(num1, num2)}")
    except ValueError as e:
        print(e)