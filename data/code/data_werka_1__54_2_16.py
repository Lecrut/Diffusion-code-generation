import math

def get_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7.0
    area_result = get_area(sample_radius)
    print(area_result)