import math

def surface_area_square_pyramid(base_length, lateral_edge_length):
    base_area = base_length ** 2
    slant_height = math.sqrt(lateral_edge_length ** 2 - (base_length / 2) ** 2)
    lateral_area = 0.5 * (4 * base_length) * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 4
    lateral_edge = 5
    result = surface_area_square_pyramid(base, lateral_edge)
    print(result)