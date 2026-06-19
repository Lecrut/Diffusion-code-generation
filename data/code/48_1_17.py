class Shape:
    def __init__(self, length, width=None):
        self.length = length
        if width is not None:
            self.width = width
        else:
            self.width = length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    side_length = 7
    rectangle_length = 8
    rectangle_width = 3

    square = Shape(side_length)
    rectangle = Shape(rectangle_length, rectangle_width)

    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
    print(f"Rectangle Area: {rectangle.area()}")