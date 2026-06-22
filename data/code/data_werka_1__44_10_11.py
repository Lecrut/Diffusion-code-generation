class Rectangle:
    def __init__(self, length, width):
        self.length = self.validate_dimension(length)
        self.width = self.validate_dimension(width)

    @staticmethod
    def validate_dimension(dimension):
        if not isinstance(dimension, (int, float)) or dimension <= 0:
            raise ValueError("Dimension must be a positive number.")
        return dimension

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rectangle = Rectangle(9, 5)
        print(rectangle.perimeter())
    except ValueError as e:
        print(e)