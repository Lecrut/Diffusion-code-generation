import math
def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width
def calculate_area_circle(radius: float) -> float:
    return math.pi * (radius ** 2)
def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height
def calculate_area_ellipse(semi_major_axis: float, semi_minor_axis: float) -> float:
    return math.pi * semi_major_axis * semi_minor_axis
if __name__ == '__main__':
    length_rect = 10.0
    width_rect = 5.0
    radius_circle = 7.0
    base_triangle = 8.0
    height_triangle = 6.0
    semi_major = 10.0
    semi_minor = 4.0
    area_rect = calculate_area_rectangle(length_rect, width_rect)
    area_circle = calculate_area_circle(radius_circle)
    area_triangle = calculate_area_triangle(base_triangle, height_triangle)
    area_ellipse = calculate_area_ellipse(semi_major, semi_minor)
    print(f"Area of rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    print(f"Area of circle (R={radius_circle}): {area_circle}")
    print(f"Area of triangle (Base={base_triangle}, Height={height_triangle}): {area_triangle}")
    print(f"Area of ellipse (a={semi_major}, b={semi_minor}): {area_ellipse}")