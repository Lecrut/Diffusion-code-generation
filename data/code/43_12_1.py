import math

def square_pyramid_surface_area(base_length: float, lateral_edge_length: float) -> float:
    base_area = base_length ** 2
    apothem = math.sqrt(lateral_edge_length ** 2 - (base_length / 2) ** 2)
    lateral_area = 2 * base_length * apothem
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_length = 6.0
    lateral_edge_length = 5.0
    result = square_pyramid_surface_area(base_length, lateral_edge_length)
    print(result)