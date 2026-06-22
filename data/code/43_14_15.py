import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 10.0
    height = 12.0
    result = calculate_square_pyramid_surface_area(side, height)
    print(result)