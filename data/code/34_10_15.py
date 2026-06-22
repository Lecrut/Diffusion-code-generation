import math

def _validate_inputs(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")

def calculate_cylinder_surface_area(radius, height):
    _validate_inputs(radius, height)
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    r = 7.5
    h = 12.0
    total_area = calculate_cylinder_surface_area(r, h)
    print(total_area)