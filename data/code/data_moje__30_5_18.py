import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    radius_value = 5.0
    area_result = calculate_circle_area(radius_value)
    print(area_result)