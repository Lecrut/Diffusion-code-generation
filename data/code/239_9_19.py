class Rectangle:
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative numbers.")
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    try:
        rect = Rectangle(5, 3)
        perimeter = Rectangle.calculate_perimeter(rect.length, rect.width)
        print(perimeter)
    except ValueError as e:
        print(e)