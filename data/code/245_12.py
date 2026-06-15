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
    print("\nComparing circle1 and rectangle1:")
    print(f"Are areas equal? {circle1.are_areas_equal(rectangle1)}")
    print("\nComparing circle1 and circle2 (should be close):")
    print(f"Area of circle2: {circle2.calculate_area()}")
    print(f"Are areas equal? {circle1.are_areas_equal(circle2)}")
    rectangle2 = Rectangle(4, 6)
    print("\nComparing rectangle1 and rectangle2 (should be equal):")
    print(f"Area of rectangle2: {rectangle2.calculate_area()}")
    print(f"Are areas equal? {rectangle1.are_areas_equal(rectangle2)}")