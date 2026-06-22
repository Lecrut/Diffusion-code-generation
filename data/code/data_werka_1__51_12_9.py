class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect1 = Rectangle(4, 6)
    perimeter1 = rect1.calculate_perimeter()
    print(perimeter1)

    rect2 = Rectangle(8, 3)
    perimeter2 = rect2.calculate_perimeter()
    print(perimeter2)