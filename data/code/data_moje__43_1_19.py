import math

def pyramid_areas(base_edge, height):
    half_base = base_edge / 2.0
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    base_area = base_edge ** 2
    lateral_area = 4 * (0.5 * base_edge * slant_height)
    total_area = base_area + lateral_area
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    base = 6.0
    h = 4.0
    results = pyramid_areas(base, h)
    print(results)