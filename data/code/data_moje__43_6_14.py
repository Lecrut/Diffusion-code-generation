import math

def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base = 5.0
    slant = 6.0
    result = surface_area_square_pyramid(base, slant)
    print(result)