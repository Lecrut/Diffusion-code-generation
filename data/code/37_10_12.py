from typing import Union

def compute_parallelogram_area(base: Union[int, float], height: Union[int, float]) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return float(base * height)

if __name__ == '__main__':
    base_value: float = 10.0
    height_value: float = 5.0
    result: float = compute_parallelogram_area(base_value, height_value)
    print(result)