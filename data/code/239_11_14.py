class Rectangle:
    def __init__(self, length=4, width=2):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(9, 5)
    perim = rect.perimeter()
    print(perim)