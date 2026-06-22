import math

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_calculator = CircleCalculator(5.0)
    area = circle_calculator.calculate_area()
    circumference = circle_calculator.circumference()
    
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)