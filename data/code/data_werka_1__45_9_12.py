import math

PI = 3.141592653589793

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def circumference(self):
        return 2 * PI * self.radius

if __name__ == '__main__':
    try:
        sample_radius1 = 5.0
        circle1 = Circle(sample_radius1)
        print(circle1.area())
        print(circle1.circumference())

        sample_radius2 = 3.0
        circle2 = Circle(sample_radius2)
        print(circle2.area())
        print(circle2.circumference())
    except ValueError as e:
        print(e)