from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b
if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))