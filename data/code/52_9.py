import math
from typing import Union
def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width
def calculate_area_circle(radius: float) -> float:
    return math.pi * (radius ** 2)
def calculate_area_triangle_right(base: float, height: float) -> float:
    return 0.5 * base * height
def calculate_area_parallelogram(base: float, height: float) -> float:
    return base * height
def calculate_area_ellipse(a: float, b: float) -> float:
    return 2 * math.pi * a * b
def calculate_area_circle_from_diameter(diameter: float) -> float:
    radius: float = diameter / 2
    return calculate_area_circle(radius)
if __name__ == '__main__':
    length_rect: float = 10.0
    width_rect: float = 5.0
    area_rect: float = calculate_area_rectangle(length_rect, width_rect)
    print(f"Area of rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    radius_circ: float = 7.0
    area_circ: float = calculate_area_circle(radius_circ)
    print(f"Area of circle (R={radius_circ}): {area_circ}")
    base_tri: float = 4.0
    height_tri: float = 6.0
    area_tri: float = calculate_area_triangle_right(base_tri, height_tri)
    print(f"Area of right triangle (Base={base_tri}, Height={height_tri}): {area_tri}")
    base_par: float = 8.0
    height_par: float = 3.0
    area_par: float = calculate_area_parallelogram(base_par, height_par)
    print(f"Area of parallelogram (Base={base_par}, Height={height_par}): {area_par}")
    a_ell: float = 3.0
    b_ell: float = 4.0
    area_ell: float = calculate_area_ellipse(a_ell, b_ell)
    print(f"Area of ellipse (a={a_ell}, b={b_ell}): {area_ell}")
    diameter_circ: float = 14.0
    area_circ_from_diam: float = calculate_area_circle_from_diameter(diameter_circ)
    print(f"Area of circle from diameter (D={diameter_circ}): {area_circ_from_diam}")