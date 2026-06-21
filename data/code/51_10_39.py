class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._validate_dimensions()

    def _validate_dimensions(self):
        if not (isinstance(self.width, (int, float)) and isinstance(self.height, (int, float))):
            raise ValueError("Width and height must be numbers.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        width = 8.5
        height = 4.2
        rect = Rectangle(width, height)
        print(rect.perimeter())
    except ValueError as e:
        print(f"Error: {e}")