import math

def square_pyramid_surface_area(base_length, lateral_edge):
    base_area = base_length ** 2
    half_base_diagonal = base_length * math.sqrt(2) / 2
    slant_height = math.sqrt(lateral_edge ** 2 - half_base_diagonal ** 2)
    lateral_surface_area = 4 * (0.5 * base_length * slant_height)
    total_surface_area = base_area + lateral_surface_area
    return total_surface_area
if __name__ == '__main__':
    base_length = 4.0
    lateral_edge = 5.0
    area = square_pyramid_surface_area(base_length, lateral_edge)
    print(area)