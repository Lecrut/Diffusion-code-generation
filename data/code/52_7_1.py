from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
if __name__ == '__main__':
    square = Square(5)
    circle = Circle(3)
    print(f"Square Area: {square.area()}")
    print(f"Circle Area: {circle.area()}")