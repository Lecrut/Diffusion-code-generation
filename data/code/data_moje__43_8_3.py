import math

def validate_positive(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value <= 0:
        raise ValueError(f"{name} must be a positive number.")

def surface_area_square_pyramid(base_side, slant_height):
    validate_positive(base_side, "base_side")
    validate_positive(slant_height, "slant_height")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 10
    slant_height = 12
    result = surface_area_square_pyramid(base_side, slant_height)
    print(result)