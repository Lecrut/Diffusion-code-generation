import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return calculate_area(self.radius)

if __name__ == '__main__':
    sample_radius = 5
    calculator_instance = CircleCalculator(sample_radius)
    print(calculator_instance.compute_area())