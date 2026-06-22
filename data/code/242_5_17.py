import math

def validate_dimensions(dimensions, expected_type):
    if not isinstance(dimensions, (tuple, list)) or len(dimensions) != 2:
        raise ValueError("Dimensions must be a tuple or list of two numbers.")
    for dim in dimensions:
        if not isinstance(dim, (int, float)) or dim <= 0:
            raise ValueError(f"{expected_type} must be a positive number.")

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    validate_dimensions((semi_major_axis, semi_minor_axis), "Semi-major and semi-minor axes")
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    validate_dimensions((base, height), "Base and height")
    return 0.5 * base * height

if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(5, 3)
    triangle_area = calculate_area_triangle(10, 4)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")