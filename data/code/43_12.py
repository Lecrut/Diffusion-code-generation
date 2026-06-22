import math

def calculate_square_pyramid_surface_area(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError('Base length and lateral edge length must be positive.')
    diagonal_half = base_length / math.sqrt(2)
    slant_height = math.sqrt(lateral_edge_length ** 2 - diagonal_half ** 2)
    if slant_height ** 2 < 0:
        raise ValueError('Invalid dimensions: lateral edge length is too short to form a pyramid.')
    base_area = base_length ** 2
    lateral_area = 4 * (0.5 * base_length * slant_height)
    return base_area + lateral_area
if __name__ == '__main__':
    base_len = 10.0
    lat_edge = 13.0
    area = calculate_square_pyramid_surface_area(base_len, lat_edge)
    print(area)