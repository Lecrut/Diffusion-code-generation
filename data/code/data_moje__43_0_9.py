import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers.")
    base_area = base_side ** 2
    triangle_area = 0.5 * base_side * slant_height
    total_lateral_area = 4 * triangle_area
    total_surface_area = base_area + total_lateral_area
    return total_surface_area

if __name__ == '__main__':
    sample_base_side = 5.0
    sample_slant_height = 8.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_slant_height)
    print(result)