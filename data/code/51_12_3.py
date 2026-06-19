class Rectangle:
    def __init__(self, dimensions):
        self.width = dimensions['width']
        self.height = dimensions['height']

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rectangle_dimensions = {'width': 7, 'height': 3}
    rect = Rectangle(rectangle_dimensions)
    perimeter = rect.calculate_perimeter()
    print(perimeter)