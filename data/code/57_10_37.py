import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * (radius ** 2)

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def compute(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    sample_radius = 5
    calculator_instance = CircleAreaCalculator(sample_radius)
    print(calculator_instance.compute())