import math

def calculate_cylinder_surface_areas(radii, heights):
    radii = list(radii)
    heights = list(heights)
    n = max(len(radii), len(heights))
    if len(radii) < n:
        radii.extend([radii[-1]] * (n - len(radii)))
    if len(heights) < n:
        heights.extend([heights[-1]] * (n - len(heights)))
    areas = []
    for r, h in zip(radii, heights):
        if r < 0 or h < 0:
            raise ValueError("Radii and heights must be non-negative")
        area = 2 * math.pi * r * (r + h)
        areas.append(area)
    return areas

if __name__ == '__main__':
    sample_radii = [1.0, 2.5, 3.0, 0.0, 10.0]
    sample_heights = [2.0, 1.0, 5.0, 0.0, 20.0]
    result = calculate_cylinder_surface_areas(sample_radii, sample_heights)
    print(result)