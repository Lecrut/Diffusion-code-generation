import math

def calculate_cylinder_surface_areas(radii, heights):
    radii = [float(r) for r in radii]
    heights = [float(h) for h in heights]
    if len(radii) != len(heights):
        raise ValueError("radii and heights must have the same length")
    results = []
    for r, h in zip(radii, heights):
        if r < 0 or h < 0:
            raise ValueError("Radii and heights must be non-negative")
        area = 2 * math.pi * r * (r + h)
        results.append(area)
    return results

if __name__ == '__main__':
    radii = [1.0, 2.5, 0.1, 1000.0]
    heights = [2.0, 1.0, 5.0, 0.001]
    surface_areas = calculate_cylinder_surface_areas(radii, heights)
    print(surface_areas)