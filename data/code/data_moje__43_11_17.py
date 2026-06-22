import math

def surface_area_square_pyramid(base_edge, height):
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 10.0
    height = 12.0
    area = surface_area_square_pyramid(base_edge, height)
    print(area)