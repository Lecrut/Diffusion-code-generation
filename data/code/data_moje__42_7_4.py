import math
from typing import Union

Number = Union[int, float]

def ellipse_area(semi_major_axis: Number, semi_minor_axis: Number) -> float:
    if semi_major_axis < 0 or semi_minor_axis < 0:
        raise ValueError("Semi-axes must be non-negative")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = ellipse_area(a, b)
    print(area)