class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    SQUARE_SIDE_LENGTH = 5
    RECTANGLE_LENGTH = 4
    RECTANGLE_WIDTH = 6

    square = Shape(SQUARE_SIDE_LENGTH)
    rectangle = Shape(RECTANGLE_LENGTH, RECTANGLE_WIDTH)

    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())