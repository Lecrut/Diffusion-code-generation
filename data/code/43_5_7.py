import math

def surface_area_of_square_pyramid(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 5.0
    slant_height = 7.0
    result = surface_area_of_square_pyramid(base_edge, slant_height)
    print(result)