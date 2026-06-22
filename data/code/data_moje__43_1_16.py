import math

def compute_square_pyramid_areas(base_edge, height):
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_edge * slant_height
    base_area = base_edge ** 2
    total_area = lateral_area + base_area
    return {
        "lateral_area": lateral_area,
        "total_area": total_area
    }

if __name__ == '__main__':
    base_edge = 5.0
    height = 6.0
    result = compute_square_pyramid_areas(base_edge, height)
    print(result)