import math

def calculate_cylinder_surface_areas(radii, heights):
    results = []
    for r, h in zip(radii, heights):
        if r < 0 or h < 0:
            raise ValueError("Radii and heights must be non-negative")
        base_area = math.pi * r * r
        lateral_area = 2 * math.pi * r * h
        surface_area = 2 * base_area + lateral_area
        results.append(surface_area)
    return results

if __name__ == '__main__':
    radii = [2.5, 3.0, 1.2]
    heights = [10.0, 5.0, 8.5]
    surface_areas = calculate_cylinder_surface_areas(radii, heights)
    print(surface_areas)