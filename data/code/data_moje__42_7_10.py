import math
from typing import Union

Number = Union[int, float]

def ellipse_area(semi_major: Number, semi_minor: Number) -> float:
    a = float(semi_major)
    b = float(semi_minor)
    if a < 0 or b < 0:
        raise ValueError("Semi-axes must be non-negative")
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Semi-axes must be finite numbers")
    return math.pi * a * b

if __name__ == '__main__':
    result = ellipse_area(5.0, 3.0)
    print(result)