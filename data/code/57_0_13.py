import math

def calculate_area_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3.5
    area_result = calculate_area_circle(sample_radius)
    print(area_result)