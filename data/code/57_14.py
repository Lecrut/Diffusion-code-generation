import math
def calculate_circle_area(radius):
    return math.pi * radius**2
if __name__ == '__main__':
    radius_value = 5.0
    area = calculate_circle_area(radius_value)
    print(area)