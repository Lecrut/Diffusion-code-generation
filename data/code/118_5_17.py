from typing import Union

CONST_MULTIPLIER = 2.0

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b * CONST_MULTIPLIER

if __name__ == '__main__':
    result = multiply(3, 4)
    print(result)