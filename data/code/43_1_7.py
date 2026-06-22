import math

def compute_pyramid_surface_area(base_edge, height):
    half_base = base_edge / 2
    slant_height = math.sqrt(half_base ** 2 + height ** 2)
    lateral_area = base_edge * slant_height
    base_area = base_edge ** 2
    total_area = lateral_area + base_area
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    base_edge = 10
    height = 12
    results = compute_pyramid_surface_area(base_edge, height)
    print(results)