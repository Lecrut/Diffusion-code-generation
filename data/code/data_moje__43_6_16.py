import math

def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    height = 6.0
    result = surface_area_square_pyramid(side, height)
    print(result)