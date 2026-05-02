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
def calculate_area_ellipse(semi_major_axis: float, semi_minor_axis: float) -> float:
    return math.pi * semi_major_axis * semi_minor_axis
def calculate_area_square(side: float) -> float:
    return side ** 2
if __name__ == '__main__':
    length_rect = 10.0
    width_rect = 5.0
    area_rect = calculate_area_rectangle(length_rect, width_rect)
    print(f"Area of rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    radius_circle = 7.0
    area_circle = calculate_area_circle(radius_circle)
    print(f"Area of circle (R={radius_circle}): {area_circle}")
    base_tri = 4.0
    height_tri = 6.0
    area_triangle = calculate_area_triangle_right(base_tri, height_tri)
    print(f"Area of right triangle (Base={base_tri}, Height={height_tri}): {area_triangle}")
    base_para = 8.0
    height_para = 3.0
    area_parallelogram = calculate_area_parallelogram(base_para, height_para)
    print(f"Area of parallelogram (Base={base_para}, Height={height_para}): {area_parallelogram}")
    semi_major = 5.0
    semi_minor = 3.0
    area_ellipse = calculate_area_ellipse(semi_major, semi_minor)
    print(f"Area of ellipse (a={semi_major}, b={semi_minor}): {area_ellipse}")
    side_square = 4.0
    area_square = calculate_area_square(side_square)
    print(f"Area of square (Side={side_square}): {area_square}")