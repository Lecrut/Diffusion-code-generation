class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    dimensions = {'length': 9, 'width': 2}
    rect = Rectangle(dimensions['length'], dimensions['width'])
    print(rect.perimeter())