import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
if __name__ == '__main__':
    radius_value = 5.0
    circle = Circle(radius_value)
    area = circle.calculate_area()
    circumference = circle.calculate_circumference()
    print(f"Radius: {radius_value}")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")