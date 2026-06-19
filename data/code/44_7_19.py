class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        try:
            length = float(self.length)
            width = float(self.width)
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive numbers.")
            return 2 * (length + width)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_length = "7"
    sample_width = "3"
    rectangle = Rectangle(sample_length, sample_width)
    perimeter = rectangle.calculate_perimeter()
    print(perimeter)