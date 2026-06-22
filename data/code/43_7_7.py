import math

def square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_area = base_area + lateral_area
    return round(total_area, 2)

if __name__ == '__main__':
    base_side = 10
    slant_height = 12
    result = square_pyramid_surface_area(base_side, slant_height)
    print(result)