import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    triangle_area = 0.5 * base_side * slant_height
    lateral_area = 4 * triangle_area
    return base_area + lateral_area

if __name__ == '__main__':
    base = 6.0
    slant = 5.0
    result = calculate_square_pyramid_surface_area(base, slant)
    print(result)