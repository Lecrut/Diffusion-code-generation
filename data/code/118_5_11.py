from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    value1 = 8
    value2 = 3.5
    result = multiply(value1, value2)
    print(result)