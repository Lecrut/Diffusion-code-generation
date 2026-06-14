import math
class Shape:
    def calculate_area(self):
        raise NotImplementedError
    def are_areas_equal(self, other_shape):
        return abs(self.calculate_area() - other_shape.calculate_area()) < 1e-9
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
if __name__ == '__main__':
    circle1 = Circle(5)
    rectangle1 = Rectangle(4, 6)
    circle2 = Circle(5.000000000000001)
    print(f"Area of circle1: {circle1.calculate_area()}")
    print(f"Area of rectangle1: {rectangle1.calculate_area()}")
    print("-" * 20)
    result1 = circle1.are_areas_equal(rectangle1)
    print(f"Are areas of circle1 and rectangle1 equal? {result1}")
    result2 = circle1.are_areas_equal(circle2)
    print(f"Are areas of circle1 and circle2 equal? {result2}")