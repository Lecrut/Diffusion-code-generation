import math

def calculate_cylinder_surface_areas(radii, heights):
    if len(radii) != len(heights):
        raise ValueError("Radii and heights arrays must have the same length")
    
    results = []
    for r, h in zip(radii, heights):
        if r < 0 or h < 0:
            raise ValueError("Radius and height must be non-negative")
        lateral_area = 2 * math.pi * r * h
        base_area = 2 * math.pi * r * r
        total_area = lateral_area + base_area
        results.append(total_area)
    return results

if __name__ == '__main__':
    sample_radii = [1.0, 2.5, 0.0, 5.0]
    sample_heights = [10.0, 3.0, 5.0, 2.0]
    areas = calculate_cylinder_surface_areas(sample_radii, sample_heights)
    print(areas)