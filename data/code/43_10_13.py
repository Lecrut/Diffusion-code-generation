import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    perimeter = 4 * base_side
    lateral_area = 0.5 * perimeter * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 5.0
    slant = 8.0
    result = calculate_square_pyramid_surface_area(base, slant)
    print(result)