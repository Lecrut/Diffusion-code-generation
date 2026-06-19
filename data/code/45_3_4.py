import math

class Circle:
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

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle1 = Circle(5.0)
        print(circle1.area())

        circle2 = Circle(3.0)
        print(circle2.area())
    except ValueError as e:
        print(e)