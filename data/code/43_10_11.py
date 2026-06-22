import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    base_perimeter = 4 * base_side
    lateral_area = 0.5 * base_perimeter * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    sample_base_side = 10.0
    sample_slant_height = 12.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_slant_height)
    print(result)