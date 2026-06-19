class Rectangle:
    def __init__(self, length, width):
        self.length = self.validate_dimension(length)
        self.width = self.validate_dimension(width)

    @staticmethod
    def validate_dimension(dimension):
        if not isinstance(dimension, (int, float)):
            raise TypeError("Dimension must be a number.")
        if dimension <= 0:
            raise ValueError("Dimension must be positive.")
        return dimension

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(9, 6)
        print(rect.get_perimeter())
    except (TypeError, ValueError) as e:
        print(e)