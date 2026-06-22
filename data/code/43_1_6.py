import math

def compute_pyramid_areas(base_edge, height):
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_area = base_area + lateral_area
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    result = compute_pyramid_areas(4, 6)
    print(result)