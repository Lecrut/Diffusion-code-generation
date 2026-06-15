import math
class Shape:
    def calculate_area(self):
        raise NotImplementedError
    def are_areas_equal(self, other_shape):
        area1 = self.calculate_area()
        area2 = other_shape.calculate_area()
        return math.isclose(area1, area2)
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
    rectangle2 = Rectangle(4.000000000000001, 6)
    shape1 = circle1
    shape2 = rectangle1
    print(f"Area of Circle 1: {shape1.calculate_area()}")
    print(f"Area of Rectangle 1: {shape2.calculate_area()}")
    print(f"Are areas of Circle 1 and Rectangle 1 equal? {shape1.are_areas_equal(shape2)}")
    shape3 = circle2
    shape4 = rectangle2
    print(f"\nArea of Circle 2: {shape3.calculate_area()}")
    print(f"Area of Rectangle 2: {shape4.calculate_area()}")
    print(f"Are areas of Circle 2 and Rectangle 2 equal? {shape3.are_areas_equal(shape4)}")
    circle3 = Circle(5)
    print(f"\nArea of Circle 3: {circle3.calculate_area()}")
    print(f"Are areas of Circle 1 and Circle 3 equal? {circle1.are_areas_equal(circle3)}")