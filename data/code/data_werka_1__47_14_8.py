from typing import NamedTuple

class Triangle(NamedTuple):
    base: float
    height: float

def calculate_triangle_area(triangle: Triangle) -> float:
    return 0.5 * triangle.base * triangle.height

if __name__ == '__main__':
    sample_triangle = Triangle(base=7.0, height=3.0)
    area = calculate_triangle_area(sample_triangle)
    print(area)