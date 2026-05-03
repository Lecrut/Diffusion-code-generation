import math
from typing import Union
def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width
def calculate_area_circle(radius: float) -> float:
    return math.pi * (radius ** 2)
def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height
def calculate_area_ellipse(a: float, b: float) -> float:
    return 2 * math.pi * a * b
def calculate_area_square(side: float) -> float:
    return side ** 2
if __name__ == '__main__':
    length_rect = 10.0
    width_rect = 5.0
    radius_circ = 7.0
    base_tri = 4.0
    height_tri = 6.0
    a_ell = 3.0
    b_ell = 4.0
    side_sq = 8.0
    area_rect = calculate_area_rectangle(length_rect, width_rect)
    area_circ = calculate_area_circle(radius_circ)
    area_tri = calculate_area_triangle(base_tri, height_tri)
    area_ell = calculate_area_ellipse(a_ell, b_ell)
    area_sq = calculate_area_square(side_sq)
    print(f"Area of Rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    print(f"Area of Circle (R={radius_circ}): {area_circ}")
    print(f"Area of Triangle (Base={base_tri}, Height={height_tri}): {area_tri}")
    print(f"Area of Ellipse (a={a_ell}, b={b_ell}): {area_ell}")
    print(f"Area of Square (Side={side_sq}): {area_sq}")