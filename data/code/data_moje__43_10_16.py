import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    slant_area = 4 * (0.5 * base_side * slant_height)
    return base_area + slant_area

if __name__ == '__main__':
    sample_base = 10.0
    sample_slant = 12.0
    result = calculate_square_pyramid_surface_area(sample_base, sample_slant)
    print(result)