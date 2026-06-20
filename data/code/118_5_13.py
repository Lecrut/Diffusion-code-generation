from typing import Union

PRODUCT_FACTOR = 1

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b * PRODUCT_FACTOR

if __name__ == '__main__':
    result = multiply(5, 10)
    print(result)