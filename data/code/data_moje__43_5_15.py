import math

def calculate_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_length = 5
    slant = 8
    result = calculate_pyramid_surface_area(base_length, slant)
    print(result)