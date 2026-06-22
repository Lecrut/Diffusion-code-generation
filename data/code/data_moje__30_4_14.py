import math

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

if __name__ == '__main__':
    sample_radius = 12.5
    calculator = CircleAreaCalculator(sample_radius)
    computed_area = calculator.compute_area()
    retrieved_radius = calculator.get_radius()
    print(computed_area)
    print(retrieved_radius)