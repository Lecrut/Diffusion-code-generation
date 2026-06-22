class Rectangle:
    MIN_DIMENSION = 1

    @staticmethod
    def validate_dimension(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def __init__(self, length, width):
        self.validate_dimension(length)
        self.validate_dimension(width)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 2
    rect = Rectangle(sample_length, sample_width)
    print(rect.perimeter())