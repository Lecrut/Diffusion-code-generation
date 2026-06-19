import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

class CircleAreaCalculator:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return calculate_circle_area(self.radius)
if __name__ == '__main__':
    test_radius = 7.5
    circle_calculator = CircleAreaCalculator(test_radius)
    area_result = circle_calculator.get_area()
    print(area_result)