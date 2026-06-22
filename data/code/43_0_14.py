import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive.")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base = 5.0
    slant = 6.0
    area = calculate_square_pyramid_surface_area(base, slant)
    print(area)