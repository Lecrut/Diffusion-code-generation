import math

def square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    triangular_faces_area = 2 * base_side * slant_height
    total_surface_area = base_area + triangular_faces_area
    return total_surface_area

if __name__ == '__main__':
    base = 6
    slant = 8
    result = square_pyramid_surface_area(base, slant)
    print(result)