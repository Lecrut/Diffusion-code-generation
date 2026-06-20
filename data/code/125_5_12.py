from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be integers or floats")
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be integers or floats")
    return a - b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))