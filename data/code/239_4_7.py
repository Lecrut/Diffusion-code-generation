class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.perimeter())