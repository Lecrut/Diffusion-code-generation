class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    WIDTH = 8
    HEIGHT = 15
    rect = Rectangle(WIDTH, HEIGHT)
    perimeter = rect.calculate_perimeter()
    print(perimeter)