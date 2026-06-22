import math

def surface_area_square_pyramid(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base_edge_length = 10.0
    slant_height_length = 15.0
    result = surface_area_square_pyramid(base_edge_length, slant_height_length)
    print(result)