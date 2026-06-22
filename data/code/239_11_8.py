class Rectangle:
    def __init__(self, length=6, width=4):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print("Length:", rect.length)
    print("Width:", rect.width)
    print("Perimeter:", rect.get_perimeter())