class Shape:
    def calculate_perimeter(self, length, width):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def calculate_perimeter(self, length, width):
        return 2 * (length + width)
class Square(Shape):
    def calculate_perimeter(self, side):
        return 4 * side
if __name__ == '__main__':
    rectangle = Rectangle()
    print("Rectangle Perimeter: " + str(rectangle.calculate_perimeter(10, 5)))
    square = Square()
    print("Square Perimeter: " + str(square.calculate_perimeter(7)))