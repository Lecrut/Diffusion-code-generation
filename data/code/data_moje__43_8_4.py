def validate_positive_number(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def calculate_square_pyramid_surface_area(base_side, slant_height):
    validate_positive_number(base_side, "base_side")
    validate_positive_number(slant_height, "slant_height")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    result = calculate_square_pyramid_surface_area(4.0, 6.0)
    print(result)