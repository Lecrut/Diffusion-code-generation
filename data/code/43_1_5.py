import math

def compute_square_pyramid_areas(base_edge, height):
    base_area = base_edge ** 2
    slant_height = math.sqrt(height ** 2 + (base_edge / 2) ** 2)
    lateral_area = 0.5 * 4 * base_edge * slant_height
    total_area = base_area + lateral_area
    return {"lateral_area": lateral_area, "total_area": total_area}

if __name__ == '__main__':
    base_edge = 4
    height = 5
    result = compute_square_pyramid_areas(base_edge, height)
    print(result)