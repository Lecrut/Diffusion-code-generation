import math

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_diameter(self):
        return self.radius * 2

    def reset_radius(self, new_radius):
        self.radius = new_radius

if __name__ == '__main__':
    calc = CircleCalculator(5)
    print(calc.get_area())
    print(calc.get_diameter())