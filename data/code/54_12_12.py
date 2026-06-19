import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(5.0)
    area1 = circle1.calculate_area()
    print(area1)