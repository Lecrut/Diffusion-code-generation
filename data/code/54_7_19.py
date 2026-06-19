import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_areas_for_radii(radii_list):
    areas = {}
    for radius in radii_list:
        areas[radius] = calculate_area(radius)
    return areas

if __name__ == '__main__':
    sample_radii = [3.0, 5.5, 7.2]
    calculated_areas = calculate_areas_for_radii(sample_radii)
    print(calculated_areas)