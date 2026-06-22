import math

def square_pyramid_surface_area(base_side, height):
    if base_side <= 0:
        raise ValueError('Base side must be positive')
    if height <= 0:
        raise ValueError('Height must be positive')
    base_area = base_side ** 2
    half_base = base_side / 2
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_area = base_area + lateral_area
    return total_area
if __name__ == '__main__':
    sample_base_side = 4.0
    sample_height = 3.0
    result = square_pyramid_surface_area(sample_base_side, sample_height)
    print(result)
    test_base_side = 10.0
    test_height = 8.0
    result2 = square_pyramid_surface_area(test_base_side, test_height)
    print(result2)
    small_base = 1.0
    small_height = 1.0
    result3 = square_pyramid_surface_area(small_base, small_height)
    print(result3)