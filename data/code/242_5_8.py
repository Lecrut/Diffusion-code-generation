import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

def compare_areas(ellipse_params, triangle_params):
    ellipse_area = calculate_area_ellipse(*ellipse_params)
    triangle_area = calculate_area_triangle(*triangle_params)
    return ellipse_area, triangle_area

if __name__ == '__main__':
    areas = compare_areas((5, 3), (10, 4))
    print(f"Ellipse area: {areas[0]}")
    print(f"Triangle area: {areas[1]}")