import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == '__main__':
    test_radius = 12.5
    area_result = calculate_circle_area(test_radius)
    print(f"The area of a circle with radius {test_radius} is {area_result}")