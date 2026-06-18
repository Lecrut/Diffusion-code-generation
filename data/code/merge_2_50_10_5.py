from typing import Union
def calculate_sum(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> int | float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError("All arguments must be numeric.") from e
if __name__ == '__main__':
    result = calculate_sum(10, 20.5, -3)
    print(result)