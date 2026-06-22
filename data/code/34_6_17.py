import math

def calculate_cylinder_surface_areas(radii, heights):
    validated_radii = [max(r, 0.0) for r in radii]
    validated_heights = [max(h, 0.0) for h in heights]
    results = []
    for r, h in zip(validated_radii, validated_heights):
        lateral_area = 2 * math.pi * r * h
        base_area = 2 * math.pi * (r ** 2)
        surface_area = lateral_area + base_area
        results.append(surface_area)
    return results

if __name__ == '__main__':
    sample_radii = [3.0, 5.5, 1.0, 0.0]
    sample_heights = [10.0, 2.0, 4.0, 0.0]
    areas = calculate_cylinder_surface_areas(sample_radii, sample_heights)
    print(areas)