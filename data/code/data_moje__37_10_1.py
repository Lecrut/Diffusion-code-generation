from typing import Union

def compute_parallelogram_area(base: float, height: float) -> float:
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return base * height

if __name__ == '__main__':
    base_value: float = 10.0
    height_value: float = 5.0
    result: float = compute_parallelogram_area(base_value, height_value)
    print(result)