from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

if __name__ == '__main__':
    num1 = 42
    num2 = 3.14
    sum_result = add_numbers(num1, num2)
    print(sum_result)