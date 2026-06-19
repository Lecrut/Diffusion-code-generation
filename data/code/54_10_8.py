import math

class Circle:
    def __init__(self, radius):
        self.radius = radius if radius >= 0 else 0

    def area(self):
        return math.pi * self.radius ** 2

    def diameter(self):
        return self.radius * 2

if __name__ == '__main__':
    circle = Circle(5)
    print(circle.area())
    print(circle.diameter())