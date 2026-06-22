import math

def calculate_cylinder_surface_areas(radii, heights):
    radii_array = [float(r) for r in radii]
    heights_array = [float(h) for h in heights]
    
    if len(radii_array) != len(heights_array):
        raise ValueError("Radii and heights arrays must have the same length")
    
    surface_areas = []
    for r, h in zip(radii_array, heights_array):
        if r < 0 or h < 0:
            raise ValueError("Radii and heights must be non-negative")
        area = 2 * math.pi * r * (r + h)
        surface_areas.append(area)
    
    return surface_areas

if __name__ == '__main__':
    sample_radii = [2.0, 5.5, 0.0, 10.0]
    sample_heights = [3.0, 2.0, 0.0, 15.0]
    results = calculate_cylinder_surface_areas(sample_radii, sample_heights)
    print(results)