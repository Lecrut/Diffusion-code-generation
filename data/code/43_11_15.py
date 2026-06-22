import math

def square_pyramid_surface_area(base_edge, height):
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_edge = 6.0
    height = 4.0
    result = square_pyramid_surface_area(base_edge, height)
    print(result)