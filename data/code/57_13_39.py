class Rectangle:
    MIN_DIMENSION = 0.1

    @staticmethod
    def validate_dimension(dimension):
        if dimension <= Rectangle.MIN_DIMENSION:
            raise ValueError("Length and width must be greater than {}".format(Rectangle.MIN_DIMENSION))

    def __init__(self, length, width):
        Rectangle.validate_dimension(length)
        Rectangle.validate_dimension(width)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    rectangle = Rectangle(sample_length, sample_width)
    area = rectangle.calculate_area()
    print(area)