import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side = 5
    slant_height = 7
    result = calculate_square_pyramid_surface_area(base_side, slant_height)
    print(result)