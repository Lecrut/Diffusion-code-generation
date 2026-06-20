from typing import Union

def add_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

if __name__ == '__main__':
    result = add_numbers(10, 5.5)
    print(f"The sum is {result}")
    result2 = add_numbers(-3, 7)
    print(f"The sum is {result2}")