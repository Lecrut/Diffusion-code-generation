class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        try:
            if not all(isinstance(x, (int, float)) for x in [self.length, self.width]):
                raise ValueError("Length and width must be numeric values.")
            if self.length <= 0 or self.width <= 0:
                raise ValueError("Length and width must be positive numbers.")
            return 2 * (self.length + self.width)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_length = '7'
    sample_width = '3.5'
    rectangle = Rectangle(sample_length, sample_width)
    perimeter = rectangle.calculate_perimeter()
    print(perimeter)