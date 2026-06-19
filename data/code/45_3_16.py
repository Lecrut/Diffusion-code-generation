import math

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius}"

if __name__ == '__main__':
    try:
        circle1 = CircleAreaCalculator(5.0)
        print(circle1.calculate_area())
        print(circle1)
        
        circle2 = CircleAreaCalculator(3.0)
        print(circle2.calculate_area())
        print(circle2)
    except ValueError as e:
        print(e)