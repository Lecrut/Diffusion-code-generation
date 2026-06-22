class Shape:
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def validate_dimensions(self):
        if not (isinstance(self.length, (int, float)) and isinstance(self.width, (int, float))):
            raise ValueError("Length and width must be numbers.")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive.")

    def perimeter(self):
        self.validate_dimensions()
        return 2 * (self.length + self.width)

    def area(self):
        self.validate_dimensions()
        return self.length * self.width

if __name__ == '__main__':
    square = Shape(5)
    rectangle = Shape(4, 6)
    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())