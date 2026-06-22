class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    rectangle = Rectangle(sample_length, sample_width)
    print(f"Perimeter of the rectangle: {Rectangle.calculate_perimeter(sample_length, sample_width)}")