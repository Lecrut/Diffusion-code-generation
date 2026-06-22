import math
from typing import Union

def calculate_ellipse_area(semi_major: Union[int, float], semi_minor: Union[int, float]) -> float:
    if semi_major < 0 or semi_minor < 0:
        raise ValueError("Semi-axes must be non-negative")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = calculate_ellipse_area(a, b)
    print(area)