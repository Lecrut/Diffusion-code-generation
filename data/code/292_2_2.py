class Shape:
    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return 4 * self.side
if __name__ == '__main__':
    rectangle = Rectangle(length=10, width=5)
    triangle = Triangle(side1=3, side2=4, side3=5)
    square = Square(side=7)
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Triangle Perimeter:", triangle.calculate_perimeter())
    print("Square Perimeter:", square.calculate_perimeter())