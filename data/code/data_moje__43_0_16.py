import math

def square_pyramid_surface_area(base_side_length, slant_height):
    if base_side_length <= 0 or slant_height <= 0:
        return 0
    base_area = base_side_length ** 2
    triangular_area = (base_side_length * slant_height) / 2
    total_surface_area = base_area + 4 * triangular_area
    return total_surface_area

if __name__ == '__main__':
    result = square_pyramid_surface_area(10, 15)
    print(result)