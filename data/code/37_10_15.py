from typing import Union

Number = Union[int, float]

def calculate_parallelogram_area(base: Number, height: Number) -> float:
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return float(base * height)

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = calculate_parallelogram_area(base_value, height_value)
    print(result)