import math

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    try:
        circle1 = Circle(5)
        area1 = circle1.calculate_area()
        print(f"Area of circle 1: {area1}")
    except ValueError as e:
        print(e)

    try:
        circle2 = Circle(-3)
        area2 = circle2.calculate_area()
        print(f"Area of circle 2: {area2}")
    except ValueError as e:
        print(e)

    try:
        circle3 = Circle(10.5)
        area3 = circle3.calculate_area()
        print(f"Area of circle 3: {area3}")
    except ValueError as e:
        print(e)