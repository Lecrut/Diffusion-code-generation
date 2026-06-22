import math

def square_pyramid_surface_area(base_length, lateral_edge_length):
    base_area = base_length ** 2
    slant_height = math.sqrt(lateral_edge_length ** 2 - (base_length / 2) ** 2)
    lateral_area = 2 * base_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 10.0
    lateral_edge = 13.0
    result = square_pyramid_surface_area(base, lateral_edge)
    print(result)