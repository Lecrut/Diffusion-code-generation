import math

def calculate_areas(radii):
    area_dict = {}
    for radius in radii:
        area = math.pi * (radius ** 2)
        area_dict[radius] = area
    return area_dict

if __name__ == '__main__':
    sample_radii = [3.0, 5.5, 7.8]
    areas = calculate_areas(sample_radii)
    print(areas)