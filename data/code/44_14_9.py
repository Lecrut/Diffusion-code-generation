class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def validate_dimensions(self):
        if not (isinstance(self.width, int) and isinstance(self.height, int)):
            raise ValueError("Width and height must be integers.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")

    def perimeter(self):
        self.validate_dimensions()
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(9, 2)
    print(rect.perimeter())