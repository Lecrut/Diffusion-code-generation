import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)

def display_shape_info(shape_instance, label):
    result = shape_instance.area()
    print(f"{label} Area: {result}")

if __name__ == '__main__':
    my_rect = Rectangle(12, 7)
    my_circle = Circle(5)

    display_shape_info(my_rect, "Rectangle")
    display_shape_info(my_circle, "Circle")