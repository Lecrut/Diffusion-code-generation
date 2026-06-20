import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    c = Circle(5)
    print(c.area())