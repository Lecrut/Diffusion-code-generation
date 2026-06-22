def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers.")
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    sample_base_side = 4.0
    sample_slant_height = 5.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_slant_height)
    print(result)