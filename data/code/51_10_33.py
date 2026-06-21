class Rectangle:
    def __init__(self, width, height):
        if not self._is_valid_dimension(width) or not self._is_valid_dimension(height):
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def _is_valid_dimension(self, dimension):
        return isinstance(dimension, (int, float)) and dimension > 0

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    sample_width = 8.0
    sample_height = 4.0
    try:
        rectangle = Rectangle(sample_width, sample_height)
        print(rectangle.perimeter())
    except ValueError as e:
        print(e)