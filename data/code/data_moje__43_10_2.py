import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side_length = 5.0
    slant_height_value = 6.0
    result = calculate_square_pyramid_surface_area(base_side_length, slant_height_value)
    print(result)