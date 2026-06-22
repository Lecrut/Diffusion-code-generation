import math
from typing import Union

def calculate_circle_area(radius: Union[int, float]) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    test_radius = 5
    area = calculate_circle_area(test_radius)
    print(area)