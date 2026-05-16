import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
if __name__ == '__main__':
    circle1 = Circle(5)
    print(f"Area of circle 1: {circle1.calculate_area()}")
    print(f"Circumference of circle 1: {circle1.calculate_circumference()}")
    circle2 = Circle(10.5)
    print(f"Area of circle 2: {circle2.calculate_area()}")
    print(f"Circumference of circle 2: {circle2.calculate_circumference()}")