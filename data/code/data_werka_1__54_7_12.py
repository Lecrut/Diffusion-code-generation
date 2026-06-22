import math

def calculate_areas(radii):
    areas = {}
    for radius in radii:
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [3.0, 7.5, 10.0]
    areas_dict = calculate_areas(sample_radii)
    for radius, area in areas_dict.items():
        print(f"Radius: {radius}, Area: {area}")