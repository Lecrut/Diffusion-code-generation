class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(9, 4)
    print(rect1.get_perimeter())

    rect2 = Rectangle(15, 7)
    print(rect2.get_perimeter())