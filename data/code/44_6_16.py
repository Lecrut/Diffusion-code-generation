class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect = Rectangle(10, 6)
    print(Rectangle.calculate_perimeter(rect.length, rect.width))