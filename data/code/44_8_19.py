class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print("Perimeter of rectangle 1:", rect1.get_perimeter())

    rect2 = Rectangle(8, 6)
    print("Perimeter of rectangle 2:", rect2.get_perimeter())