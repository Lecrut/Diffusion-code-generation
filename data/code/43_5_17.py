import math

def calculate_square_pyramid_surface_area(base_length, slant_height):
    base_area = base_length * base_length
    lateral_area = 2 * base_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_len = 4
    slant_ht = 5
    result = calculate_square_pyramid_surface_area(base_len, slant_ht)
    print(result)