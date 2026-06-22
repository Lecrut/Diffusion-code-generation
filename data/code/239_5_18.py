class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 5
    rectangle = Rectangle(sample_length, sample_width)
    perimeter = Rectangle.calculate_perimeter(sample_length, sample_width)
    print(perimeter)