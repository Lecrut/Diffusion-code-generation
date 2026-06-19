import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    circle_radius = 5
    area_of_circle = calculate_circle_area(circle_radius)
    print(area_of_circle)