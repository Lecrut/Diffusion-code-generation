import math

def calculate_cylinder_surface_area(radii, heights):
    surface_areas = []
    for r, h in zip(radii, heights):
        surface_area = 2 * math.pi * r * (r + h)
        surface_areas.append(surface_area)
    return surface_areas

if __name__ == '__main__':
    radii_sample = [1.0, 2.0, 3.0, 5.0]
    heights_sample = [4.0, 5.0, 6.0, 10.0]
    result = calculate_cylinder_surface_area(radii_sample, heights_sample)
    print(result)