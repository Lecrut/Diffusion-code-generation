class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    rectangle = Rectangle(length, width)
    perimeter = Rectangle.calculate_perimeter(length, width)
    print(perimeter)