import math
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area
if __name__ == '__main__':
    radius_value = 5.0
    area_result = calculate_circle_area(radius_value)
    print(area_result)