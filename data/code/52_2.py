class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print("Circle Area:", circle.calculate_area())
    print("Rectangle Area:", rectangle.calculate_area())