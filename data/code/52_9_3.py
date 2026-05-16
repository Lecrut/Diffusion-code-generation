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
    area_rect = calculate_area_rectangle(length_rect, width_rect)
    print(f"Area of rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    radius_circ = 7.0
    area_circ = calculate_area_circle(radius_circ)
    print(f"Area of circle (R={radius_circ}): {area_circ}")
    base_tri = 4.0
    height_tri = 6.0
    area_tri = calculate_area_triangle(base_tri, height_tri)
    print(f"Area of triangle (Base={base_tri}, Height={height_tri}): {area_tri}")
    a_ell = 3.0
    b_ell = 4.0
    area_ell = calculate_area_ellipse(a_ell, b_ell)
    print(f"Area of ellipse (a={a_ell}, b={b_ell}): {area_ell}")
    side_sq = 8.0
    area_sq = calculate_area_square(side_sq)
    print(f"Area of square (Side={side_sq}): {area_sq}")