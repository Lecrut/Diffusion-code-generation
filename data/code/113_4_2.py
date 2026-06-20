from typing import Union

def subtract_values(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

if __name__ == '__main__':
    result = subtract_values(10, 5)
    print(result)