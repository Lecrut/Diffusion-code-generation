import math

def calculate_circle_areas(radii):
    areas = {}
    for radius in radii:
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [3.0, 7.5, 10.0]
    calculated_areas = calculate_circle_areas(sample_radii)
    for radius, area in calculated_areas.items():
        print(f"Radius: {radius}, Area: {area}")