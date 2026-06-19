class Rectangle:
    def __init__(self, dimensions):
        self.length = dimensions['length']
        self.width = dimensions['width']

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_dimensions = {'length': 8, 'width': 6}
    rect = Rectangle(sample_dimensions)
    print(rect.get_perimeter())