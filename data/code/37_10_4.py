from typing import Union

Number = Union[int, float]

def calculate_parallelogram_area(base: Number, height: Number) -> Number:
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base <= 0:
        raise ValueError("Base must be greater than zero")
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = calculate_parallelogram_area(sample_base, sample_height)
    print(result)