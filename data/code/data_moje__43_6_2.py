import math

def square_pyramid_surface_area(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 10.0
    slant_height = 12.0
    result = square_pyramid_surface_area(base_edge, slant_height)
    print(result)