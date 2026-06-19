class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rectangle_dimensions = {'width': 8, 'height': 6}
    rect = Rectangle(rectangle_dimensions['width'], rectangle_dimensions['height'])
    perimeter = rect.calculate_perimeter()
    print(perimeter)