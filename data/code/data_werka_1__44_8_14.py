class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect_length = 15
    rect_width = 7
    rectangle = Rectangle(rect_length, rect_width)
    perimeter = rectangle.get_perimeter()
    print(perimeter)