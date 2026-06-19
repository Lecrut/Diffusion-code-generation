class Rectangle:
    def __init__(self, length, width):
        if not (isinstance(length, (int, float)) and length > 0):
            raise ValueError("Length must be a positive number.")
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError("Width must be a positive number.")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 15
    sample_width = 6
    rect = Rectangle(sample_length, sample_width)
    print(rect.perimeter())