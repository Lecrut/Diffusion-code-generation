import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius1 = 3.0
    area1 = calculate_circle_area(sample_radius1)
    print(area1)
    sample_radius2 = 7.5
    area2 = calculate_circle_area(sample_radius2)
    print(area2)