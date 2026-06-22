import math

def surface_area_square_pyramid(base_length, lateral_edge_length):
    base_area = base_length ** 2
    slant_height = math.sqrt(lateral_edge_length ** 2 - (base_length / 2) ** 2)
    lateral_area = 4 * (0.5 * base_length * slant_height)
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base = 10.0
    edge = 13.0
    result = surface_area_square_pyramid(base, edge)
    print(result)