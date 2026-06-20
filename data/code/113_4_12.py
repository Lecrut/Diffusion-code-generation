from typing import Union

def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(10, 5)
    print(result)