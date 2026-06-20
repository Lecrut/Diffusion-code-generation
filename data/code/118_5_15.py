from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be int or float")
    return a * b

if __name__ == '__main__':
    result = multiply(3, 4.5)
    print(result)