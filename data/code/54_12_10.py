import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle = Circle(5.0)
    print(circle.area())