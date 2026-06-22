import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_instance = Circle(5)
    print(circle_instance.area())
    print(circle_instance.circumference())