class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.validate_dimensions()

    def validate_dimensions(self):
        if not (isinstance(self.length, (int, float)) and self.length > 0):
            raise ValueError("Length must be a positive number.")
        if not (isinstance(self.width, (int, float)) and self.width > 0):
            raise ValueError("Width must be a positive number.")

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(9.5, 3.2)
        print(rect.perimeter())
    except ValueError as e:
        print(e)