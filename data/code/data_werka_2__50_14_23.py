import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def absolute_difference_in_areas(radius1, radius2):
    area1 = calculate_circle_area(radius1)
    area2 = calculate_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    radius1 = 5
    radius2 = 3
    result = absolute_difference_in_areas(radius1, radius2)
    print(result)