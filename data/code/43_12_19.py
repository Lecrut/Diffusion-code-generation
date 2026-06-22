import math

def calculate_square_pyramid_surface_area(base_length, lateral_edge_length):
    base_area = base_length ** 2
    side_length = base_length
    slant_height = math.sqrt(lateral_edge_length ** 2 - (side_length / 2) ** 2)
    lateral_area = 0.5 * 4 * side_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 10.0
    lateral_edge = 13.0
    result = calculate_square_pyramid_surface_area(base, lateral_edge)
    print(result)