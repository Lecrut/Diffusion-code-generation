import math

class Circle:
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be an integer or float")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(5.0)
    area1 = circle1.area()
    print(f"Area of circle with radius 5.0: {area1}")

    circle2 = Circle(10.5)
    area2 = circle2.area()
    print(f"Area of circle with radius 10.5: {area2}")