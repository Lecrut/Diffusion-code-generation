import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    RADIUS_1 = 5.0
    circle1 = Circle(RADIUS_1)
    area1 = circle1.area()
    print(f"Area of circle with radius {RADIUS_1}: {area1}")

    RADIUS_2 = 10.5
    circle2 = Circle(RADIUS_2)
    area2 = circle2.area()
    print(f"Area of circle with radius {RADIUS_2}: {area2}")