from typing import Union

def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(3, 4.5)
    print(result)