import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 7.0
    area = calculate_circle_area(sample_radius)
    print(area)