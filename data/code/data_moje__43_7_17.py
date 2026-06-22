import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    triangular_area = 2 * base_side * slant_height
    total_surface_area = base_area + triangular_area
    return round(total_surface_area, 2)

if __name__ == '__main__':
    base_side_length = 10
    slant_height_value = 15
    result = calculate_square_pyramid_surface_area(base_side_length, slant_height_value)
    print(result)