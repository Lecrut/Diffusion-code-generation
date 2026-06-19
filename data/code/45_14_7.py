import math

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def diameter(self):
        return 2 * self.radius
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 3
    calculator = CircleCalculator(sample_radius)
    print("Area:", calculator.area())
    print("Diameter:", calculator.diameter())
    print("Circumference:", calculator.circumference())