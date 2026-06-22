import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    radius_sample = 5
    area = calculate_circle_area(radius_sample)
    print(area)
    radius_sample_2 = 10
    area_2 = calculate_circle_area(radius_sample_2)
    print(area_2)