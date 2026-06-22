class Rectangle:

    def __init__(self, length, width):
        self.length = self._validate_dimension(length)
        self.width = self._validate_dimension(width)

    @staticmethod
    def _validate_dimension(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError('Length and width must be positive numbers.')
        return value

    def perimeter(self):
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    try:
        rect = Rectangle(9, 3)
        print(f'Perimeter of the rectangle: {rect.perimeter()}')
        another_rect = Rectangle(15, 7)
        print(f'Perimeter of another rectangle: {another_rect.perimeter()}')
    except ValueError as e:
        print(e)