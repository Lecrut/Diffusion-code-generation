class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.validate_dimensions()

    def validate_dimensions(self):
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise ValueError("Length must be a positive number.")
        if not isinstance(self.width, (int, float)) or self.width <= 0:
            raise ValueError("Width must be a positive number.")

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(15, 10)
        print(rect.perimeter())
    except ValueError as e:
        print(e)