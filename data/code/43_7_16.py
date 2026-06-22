import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_area = base_area + lateral_area
    return round(total_area, 2)

if __name__ == '__main__':
    side_length = 5.0
    slant = 8.0
    result = calculate_square_pyramid_surface_area(side_length, slant)
    print(result)