import math

def calculate_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3
    area_result = calculate_area(sample_radius)
    print(area_result)