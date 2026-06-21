import math
from typing import Union

Number = Union[int, float]

def calculate_circle_area(radius: Number) -> Number:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == "__main__":
    test_radius = 5.0
    area = calculate_circle_area(test_radius)
    print(area)