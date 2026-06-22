import math
import itertools

def calculate_cylinder_surface_areas(radii, heights):
    if len(radii) != len(heights):
        raise ValueError("Radii and heights arrays must have the same length")
    
    if not radii:
        return []
    
    areas = []
    for r, h in zip(radii, heights):
        if r < 0 or h < 0:
            raise ValueError("Radius and height must be non-negative")
        base_area = math.pi * r * r
        lateral_area = 2 * math.pi * r * h
        total_area = 2 * base_area + lateral_area
        areas.append(total_area)
    
    return areas

if __name__ == '__main__':
    sample_radii = [1.0, 2.5, 0.0, 10.0]
    sample_heights = [5.0, 3.0, 0.0, 100.0]
    
    results = calculate_cylinder_surface_areas(sample_radii, sample_heights)
    print(results)