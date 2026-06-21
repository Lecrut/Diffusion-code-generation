class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    dimensions = {'width': 5.0, 'height': 3.0}
    rect = Rectangle(dimensions['width'], dimensions['height'])
    print(rect.perimeter())