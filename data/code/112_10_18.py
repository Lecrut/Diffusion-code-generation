from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

if __name__ == '__main__':
    num1 = 20
    num2 = 35
    sum_result = add_numbers(num1, num2)
    print(sum_result)