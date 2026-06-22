import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 4.0
    slant_height = 5.0
    area = calculate_square_pyramid_surface_area(base_side, slant_height)
    print(area)