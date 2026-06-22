import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7.5
    area_result = calculate_circle_area(sample_radius)
    print(area_result)