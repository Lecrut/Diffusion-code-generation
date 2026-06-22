import math

def calculate_pyramid_surface_area(base_side_length, slant_height):
    if base_side_length <= 0 or slant_height <= 0:
        raise ValueError("Base side length and slant height must be positive numbers")
    base_area = base_side_length ** 2
    perimeter = 4 * base_side_length
    lateral_area = 0.5 * perimeter * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    sample_base = 5.0
    sample_slant = 8.0
    result = calculate_pyramid_surface_area(sample_base, sample_slant)
    print(result)