import math
from typing import Union

def calculate_ellipse_area(semi_major: Union[int, float], semi_minor: Union[int, float]) -> float:
    a = float(semi_major)
    b = float(semi_minor)

    if a < 0 or b < 0:
        raise ValueError("Semi-axes must be non-negative")

    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Semi-axes must be finite numbers")

    if a == 0 or b == 0:
        return 0.0

    return math.pi * a * b

if __name__ == '__main__':
    major = 5.0
    minor = 3.0
    area = calculate_ellipse_area(major, minor)
    print(area)