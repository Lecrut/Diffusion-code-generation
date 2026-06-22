class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def _validate_dimensions(self):
        if not isinstance(self.width, int) or not isinstance(self.height, int):
            raise ValueError("Width and height must be integers.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")

    def perimeter(self):
        self._validate_dimensions()
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(12, 8)
        print(rect.perimeter())
    except ValueError as e:
        print(e)