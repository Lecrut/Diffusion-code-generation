import math

def square_pyramid_total_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 4 * (base_side * slant_height / 2)
    total_area = base_area + lateral_area
    return round(total_area, 2)

if __name__ == '__main__':
    base = 6
    slant = 5
    result = square_pyramid_total_surface_area(base, slant)
    print(result)