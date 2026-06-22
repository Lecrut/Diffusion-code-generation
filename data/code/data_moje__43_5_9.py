import math

def square_pyramid_surface_area(base_edge: float, height: float) -> float:
    half_base = base_edge / 2
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 10.0
    height = 12.0
    area = square_pyramid_surface_area(base_edge, height)
    print(area)