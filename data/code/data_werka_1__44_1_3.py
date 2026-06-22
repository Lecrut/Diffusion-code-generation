class Rectangle:
    def __init__(self, length, width):
        self.length = self.validate_dimension(length)
        self.width = self.validate_dimension(width)

    @staticmethod
    def validate_dimension(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return value

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(8, 6)
        print(rect.perimeter())
    except ValueError as e:
        print(e)