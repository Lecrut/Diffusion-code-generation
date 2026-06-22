def calculate_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers.")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side_value = 6
    slant_height_value = 10
    result = calculate_pyramid_surface_area(base_side_value, slant_height_value)
    print(result)