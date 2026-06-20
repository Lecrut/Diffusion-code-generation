import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    radius_1 = 5
    radius_2 = 10.5
    print(calculate_circle_area(radius_1))
    print(calculate_circle_area(radius_2))