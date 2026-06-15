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
    rectangle1 = Rectangle(4, 5)
    circle2 = Circle(5)
    rectangle2 = Rectangle(5, 4)
    print("Circle 1 Area:", circle1.calculate_area())
    print("Rectangle 1 Area:", rectangle1.calculate_area())
    print("Circle 2 Area:", circle2.calculate_area())
    print("Rectangle 2 Area:", rectangle2.calculate_area())
    print("\nComparing Circle 1 and Circle 2:")
    print("Areas are equal:", circle1.are_areas_equal(circle2))
    print("\nComparing Rectangle 1 and Rectangle 2:")
    print("Areas are equal:", rectangle1.are_areas_equal(rectangle2))
    print("\nComparing Circle 1 and Rectangle 1:")
    print("Areas are equal:", circle1.are_areas_equal(rectangle1))