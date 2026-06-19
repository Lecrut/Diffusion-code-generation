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
        sample_length = 9
        sample_width = 3
        rect = Rectangle(sample_length, sample_width)
        print(rect.get_perimeter())
    except Exception as e:
        print(e)