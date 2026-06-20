from typing import Union
MIN_VALUE: int = -1000

def subtract_values(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if a < MIN_VALUE or b < MIN_VALUE:
        raise ValueError('Values must be greater than or equal to -1000')
    return a - b
if __name__ == '__main__':
    try:
        result = subtract_values(10, 5)
        print(result)
    except ValueError as e:
        print(e)