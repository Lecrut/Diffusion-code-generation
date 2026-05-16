import math
def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width
def calculate_area_circle(radius: float) -> float:
    return math.pi * (radius ** 2)
def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height
def calculate_area_ellipse(a: float, b: float) -> float:
    return 2 * math.pi * a * b
if __name__ == '__main__':
    length_rect: float = 10.0
    width_rect: float = 5.0
    radius_circ: float = 7.0
    base_tri: float = 4.0
    height_tri: float = 6.0
    semi_major_axis: float = 4.0
    semi_minor_axis: float = 3.0
    area_rect: float = calculate_area_rectangle(length_rect, width_rect)
    area_circ: float = calculate_area_circle(radius_circ)
    area_tri: float = calculate_area_triangle(base_tri, height_tri)
    area_ellipse: float = calculate_area_ellipse(semi_major_axis, semi_minor_axis)
    print(f"Area of rectangle (L={length_rect}, W={width_rect}): {area_rect}")
    print(f"Area of circle (R={radius_circ}): {area_circ}")
    print(f"Area of triangle (Base={base_tri}, Height={height_tri}): {area_tri}")
    print(f"Area of ellipse (a={semi_major_axis}, b={semi_minor_axis}): {area_ellipse}")