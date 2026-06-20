from typing import Union

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

if __name__ == '__main__':
    result = subtract(25, 10)
    print(result)