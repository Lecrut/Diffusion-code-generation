from typing import Union

def add_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

if __name__ == '__main__':
    a = 30
    b = 45.75
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")
    
    x = -10
    y = 20.25
    result2 = add_numbers(x, y)
    print(f"The sum of {x} and {y} is {result2}")