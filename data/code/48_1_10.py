class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

    @staticmethod
    def calculate_area(length, width):
        return length * width

    def perimeter(self):
        return Shape.calculate_perimeter(self.length, self.width)

    def area(self):
        return Shape.calculate_area(self.length, self.width)

if __name__ == '__main__':
    square = Shape(7)
    rectangle = Shape(3, 9)
    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())