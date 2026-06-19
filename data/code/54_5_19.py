import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Area: {circle.area()}")
    print(f"Circumference: {circle.circumference()}")