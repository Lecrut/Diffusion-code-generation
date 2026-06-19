import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    test_radius = 4.0
    computed_area = calculate_circle_area(test_radius)
    print(f"The area of a circle with radius {test_radius} is {computed_area}")