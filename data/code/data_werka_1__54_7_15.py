import math

def calculate_areas(radii):
    areas = {}
    for radius in radii:
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [3.0, 5.0, 7.5]
    calculated_areas = calculate_areas(sample_radii)
    print(calculated_areas)