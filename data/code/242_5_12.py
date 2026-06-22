import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    if not (isinstance(semi_major_axis, (int, float)) and isinstance(semi_minor_axis, (int, float))):
        raise ValueError("Semi-major and semi-minor axes must be numbers.")
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive.")
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        ellipse_area = calculate_area_ellipse(5, 3)
        triangle_area = calculate_area_triangle(10, 4)
        print(f"Ellipse area: {ellipse_area}")
        print(f"Triangle area: {triangle_area}")
    except ValueError as e:
        print(e)