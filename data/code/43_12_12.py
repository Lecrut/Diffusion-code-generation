import math

def square_pyramid_surface_area(base_length, lateral_edge_length):
    base_area = base_length ** 2
    half_base = base_length / 2.0
    slant_height = math.sqrt(lateral_edge_length ** 2 - half_base ** 2)
    triangular_area = 0.5 * base_length * slant_height
    lateral_area = 4 * triangular_area
    return base_area + lateral_area

if __name__ == '__main__':
    base_len = 4.0
    lat_edge = 5.0
    area = square_pyramid_surface_area(base_len, lat_edge)
    print(area)