class Shape:
    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return 4 * self.side
if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    square = Square(7)
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Square Perimeter:", square.calculate_perimeter())