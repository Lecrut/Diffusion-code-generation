import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return calculate_circle_area(self.radius)
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5
    calculator_instance = CircleCalculator(sample_radius)
    print("Area:", calculator_instance.area())
    print("Circumference:", calculator_instance.circumference())