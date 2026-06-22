import math

def calculate_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers")
    base_area = base_side * base_side
    base_perimeter = 4 * base_side
    lateral_area = 0.5 * base_perimeter * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side_length = 10.0
    height_slant = 15.0
    total_area = calculate_pyramid_surface_area(side_length, height_slant)
    print(total_area)