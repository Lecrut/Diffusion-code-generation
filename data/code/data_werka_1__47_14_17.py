from typing import NamedTuple

class Triangle(NamedTuple):
    base: float
    height: float

def calculate_triangle_area(triangle: Triangle) -> float:
    if triangle.base <= 0 or triangle.height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * triangle.base * triangle.height

if __name__ == '__main__':
    sample_triangle = Triangle(base=20.0, height=10.0)
    area = calculate_triangle_area(sample_triangle)
    print(area)