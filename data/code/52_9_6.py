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
    radius_circ = 7.0
    base_tri = 4.0
    height_tri = 6.0
    semi_major = 5.0
    semi_minor = 3.0
    area_rect = calculate_area_rectangle(length_rect, width_rect)
    area_circ = calculate_area_circle(radius_circ)
    area_tri = calculate_area_triangle(base_tri, height_tri)
    area_ellipse = calculate_area_ellipse(semi_major, semi_minor)
    print(f"Area of Rectangle: {area_rect}")
    print(f"Area of Circle: {area_circ}")
    print(f"Area of Triangle: {area_tri}")
    print(f"Area of Ellipse: {area_ellipse}")