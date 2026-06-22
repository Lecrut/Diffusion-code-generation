def validate_and_calculate_surface_area(base_side, slant_height):
    if not isinstance(base_side, (int, float)) or not isinstance(slant_height, (int, float)):
        raise TypeError("Base side and slant height must be numbers.")
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers.")
    
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    surface_area = base_area + lateral_area
    return surface_area

if __name__ == '__main__':
    result = validate_and_calculate_surface_area(5, 7)
    print(result)