class Rectangle:
    MIN_DIMENSION = 0.01

    @staticmethod
    def validate_dimension(dimension):
        if dimension <= Rectangle.MIN_DIMENSION:
            raise ValueError("Length and width must be greater than 0.01")

    def __init__(self, length, width):
        self.validate_dimension(length)
        self.validate_dimension(width)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    sample_length = 8.0
    sample_width = 4.5
    rectangle = Rectangle(sample_length, sample_width)
    print(rectangle.area())