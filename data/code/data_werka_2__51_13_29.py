class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.validate_dimensions()

    def validate_dimensions(self):
        if not isinstance(self.length, (int, float)) or not isinstance(self.width, (int, float)):
            raise ValueError("Length and width must be numbers.")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 6
    rect = Rectangle(sample_length, sample_width)
    print(rect.perimeter())