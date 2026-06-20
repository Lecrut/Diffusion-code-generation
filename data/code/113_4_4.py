from typing import Union

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract(10, 5)
    print(result)