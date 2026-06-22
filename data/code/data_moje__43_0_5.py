def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    sample_base_side = 5.0
    sample_slant_height = 7.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_slant_height)
    print(result)