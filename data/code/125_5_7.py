from typing import Union
ADDITION = '+'
SUBTRACTION = '-'

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    sum_result = add(num1, num2)
    diff_result = subtract(num1, num2)
    print(f'Addition: {sum_result}')
    print(f'Subtraction: {diff_result}')