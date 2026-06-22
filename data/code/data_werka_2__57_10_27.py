import math

class AreaCalculator:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 5
    calculator_instance = AreaCalculator(sample_radius)
    print(calculator_instance.calculate_circle_area())