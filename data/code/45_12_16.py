import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    circle1 = Circle(5)
    area1 = Circle.calculate_area(circle1.radius)
    print(f"Area of circle 1: {area1}")
    circle2 = Circle(10.5)
    area2 = Circle.calculate_area(circle2.radius)
    print(f"Area of circle 2: {area2}")