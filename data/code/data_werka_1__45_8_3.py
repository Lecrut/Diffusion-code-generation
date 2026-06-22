import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(10)
        print(circle.area())
    except ValueError as e:
        print(e)