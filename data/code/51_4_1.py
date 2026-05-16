import math
def calculate_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
if __name__ == '__main__':
    radius_value = 5.0
    perimeter_result = calculate_circle_perimeter(radius_value)
    print(perimeter_result)