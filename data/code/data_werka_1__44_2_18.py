class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rectangle = Shape(15, 8)
    print(rectangle.perimeter())