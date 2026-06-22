import math

def square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 6
    slant_height = 5
    result = square_pyramid_surface_area(base_side, slant_height)
    print(result)