import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    test_radius_1 = 2.5
    test_radius_2 = 7.0
    test_radius_3 = 10.0

    print("Area of circle with radius", test_radius_1, "is:", calculate_circle_area(test_radius_1))
    print("Area of circle with radius", test_radius_2, "is:", calculate_circle_area(test_radius_2))
    print("Area of circle with radius", test_radius_3, "is:", calculate_circle_area(test_radius_3))

    calculator = CircleAreaCalculator(test_radius_1)
    print("Using class method, area of circle with radius", test_radius_1, "is:", calculator.get_area())