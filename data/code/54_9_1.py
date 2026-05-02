import math
def calculate_areas(radii):
    area_dict = {}
    for r in radii:
        area = math.pi * (r ** 2)
        area_dict[r] = area
    return area_dict
if __name__ == '__main__':
    sample_radii = [1.0, 2.5, 5.0, 10.0]
    results = calculate_areas(sample_radii)
    print(results)