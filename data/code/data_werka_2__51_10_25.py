class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    WIDTH = 8.0
    HEIGHT = 4.0
    rect = Rectangle(WIDTH, HEIGHT)
    print(rect.perimeter())