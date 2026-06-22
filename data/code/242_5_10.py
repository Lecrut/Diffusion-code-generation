import math

def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    if value <= 0:
        raise ValueError("Value must be positive.")

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    validate_number(semi_major_axis)
    validate_number(semi_minor_axis)
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    validate_number(base)
    validate_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(5, 3)
    triangle_area = calculate_area_triangle(10, 4)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")