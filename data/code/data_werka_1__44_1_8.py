class Rectangle:
    def __init__(self, length, width):
        self.length = self._validate_dimension(length)
        self.width = self._validate_dimension(width)

    def _validate_dimension(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return value

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(9, 3)
    print(rect1.perimeter())

    rect2 = Rectangle(6.5, 4.2)
    print(rect2.perimeter())