class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    rectangle_area = rectangle.calculate_area()
    circle_area = circle.calculate_area()
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")