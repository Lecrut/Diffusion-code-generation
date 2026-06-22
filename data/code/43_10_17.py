import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive values")
    base_area = base_side ** 2
    triangle_area = 0.5 * base_side * slant_height
    lateral_area = 4 * triangle_area
    return base_area + lateral_area

if __name__ == '__main__':
    side_length = 10
    height_slant = 13
    total_area = calculate_square_pyramid_surface_area(side_length, height_slant)
    print(total_area)