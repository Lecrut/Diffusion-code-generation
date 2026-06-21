import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        sample_circle = Circle(10)
        print("Area of the circle:", sample_circle.area())
        print("Circumference of the circle:", sample_circle.circumference())
    except ValueError as e:
        print(e)