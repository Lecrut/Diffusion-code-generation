def validate_positive(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def calculate_square_pyramid_surface_area(base_side, slant_height):
    validate_positive(base_side, "base_side")
    validate_positive(slant_height, "slant_height")
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 5
    height = 7
    result = calculate_square_pyramid_surface_area(side, height)
    print(result)