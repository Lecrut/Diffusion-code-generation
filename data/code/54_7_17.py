import math

def calculate_areas(radii):
    areas = {}
    for radius in radii:
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [1, 2.5, 3.75]
    calculated_areas = calculate_areas(sample_radii)
    print(calculated_areas)