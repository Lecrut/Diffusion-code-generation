class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rectangle_width = 8
    rectangle_height = 6
    rect = Rectangle(rectangle_width, rectangle_height)
    perimeter = rect.calculate_perimeter()
    print(perimeter)