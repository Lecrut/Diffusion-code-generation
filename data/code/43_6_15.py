import math

def surface_area_of_square_pyramid(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge_value = 10
    slant_height_value = 15
    result = surface_area_of_square_pyramid(base_edge_value, slant_height_value)
    print(result)