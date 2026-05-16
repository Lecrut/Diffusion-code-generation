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
    radius_circle: float = 7.0
    area_circle: float = calculate_area_circle(radius_circle)
    print(f"Area of circle (R={radius_circle}): {area_circle}")
    base_tri: float = 4.0
    height_tri: float = 6.0
    area_triangle: float = calculate_area_triangle_right(base_tri, height_tri)
    print(f"Area of right triangle (Base={base_tri}, Height={height_tri}): {area_triangle}")
    base_para: float = 8.0
    height_para: float = 3.0
    area_parallelogram: float = calculate_area_parallelogram(base_para, height_para)
    print(f"Area of parallelogram (Base={base_para}, Height={height_para}): {area_parallelogram}")
    a_ellipse: float = 4.0
    b_ellipse: float = 2.0
    area_ellipse: float = calculate_area_ellipse(a_ellipse, b_ellipse)
    print(f"Area of ellipse (a={a_ellipse}, b={b_ellipse}): {area_ellipse}")
    diameter_circle: float = 14.0
    area_circle_from_diameter: float = calculate_area_circle_from_diameter(diameter_circle)
    print(f"Area of circle from diameter (D={diameter_circle}): {area_circle_from_diameter}")