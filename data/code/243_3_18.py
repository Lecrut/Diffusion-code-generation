import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_circumference(radius):
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    circle1 = Circle(5)
    print(circle1.calculate_circumference(circle1.radius))
    circle2 = Circle(10.5)
    print(circle2.calculate_circumference(circle2.radius))