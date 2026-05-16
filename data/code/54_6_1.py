import math
def area_from_diameter(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area
if __name__ == '__main__':
    sample_diameter = 10
    result_area = area_from_diameter(sample_diameter)
    print(result_area)