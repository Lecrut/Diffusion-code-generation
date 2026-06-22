from typing import Union
Number = Union[int, float]
TRIANGLE_AREA_FACTOR = 0.5
def calculate_triangle_area(base: Number, height: Number) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return TRIANGLE_AREA_FACTOR * base * height
if __name__ == '__main__':
    sample_base = 12
    sample_height = 8
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)