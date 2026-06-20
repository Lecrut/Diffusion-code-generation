from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    result = multiply(7, 2.5)
    print(result)