import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    height = 5.0
    result = calculate_square_pyramid_surface_area(side, height)
    print(result)