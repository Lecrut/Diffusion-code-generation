import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    test_radius = 5
    area = calculate_circle_area(test_radius)
    print(area)