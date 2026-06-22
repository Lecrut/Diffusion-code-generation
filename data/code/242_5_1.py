import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(5, 3)
    triangle_area = calculate_area_triangle(10, 4)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")