import math

def compute_pyramid_areas(base_edge, height):
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_edge * slant_height
    total_area = base_area + lateral_area
    return {"lateral_area": lateral_area, "total_area": total_area}

if __name__ == '__main__':
    base_edge = 10
    height = 12
    result = compute_pyramid_areas(base_edge, height)
    print(result)