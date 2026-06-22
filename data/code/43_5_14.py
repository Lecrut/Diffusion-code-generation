def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side_length = 4.0
    slant_height_value = 5.0
    result = calculate_square_pyramid_surface_area(side_length, slant_height_value)
    print(result)