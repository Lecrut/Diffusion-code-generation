def validate_and_calculate_surface_area(base_side, slant_height):
    if not isinstance(base_side, (int, float)) or not isinstance(slant_height, (int, float)):
        raise TypeError("base_side and slant_height must be numbers")
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("base_side and slant_height must be positive numbers")
    base_area = base_side * base_side
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    result = validate_and_calculate_surface_area(5, 8)
    print(result)
    try:
        validate_and_calculate_surface_area(-2, 5)
    except ValueError as e:
        print(e)