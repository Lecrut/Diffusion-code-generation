import math
from typing import Union

Number = Union[int, float]

def calculate_circle_area(radius: Number) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_1 = 5
    sample_radius_2 = 10.5
    area_1 = calculate_circle_area(sample_radius_1)
    area_2 = calculate_circle_area(sample_radius_2)
    print(area_1)
    print(area_2)