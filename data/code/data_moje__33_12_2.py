import math
from typing import Union

Number = Union[int, float]

def calculate_triangle_area(base: Number, height: Number) -> Number:
    if base < 0:
        raise ValueError("Base cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 0.5 * base * height

if __name__ == '__main__':
    base_val = 10
    height_val = 5
    result = calculate_triangle_area(base_val, height_val)
    print(result)