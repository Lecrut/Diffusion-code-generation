import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    perimeter = 4 * base_side
    lateral_area = 0.5 * perimeter * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    sample_base = 6.0
    sample_slant = 5.0
    result = calculate_square_pyramid_surface_area(sample_base, sample_slant)
    print(result)