import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == '__main__':
    test_radius = 7.0
    computed_area = calculate_circle_area(test_radius)
    print(computed_area)