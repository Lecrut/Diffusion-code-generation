from typing import Union
def add_numbers(a: float, b: float) -> float:
    return a + b
if __name__ == '__main__':
    num1 = 42.5
    num2 = 37.8
    result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")