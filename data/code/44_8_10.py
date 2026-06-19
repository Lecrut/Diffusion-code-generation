class Rectangle:
    def __init__(self, **kwargs):
        self.length = kwargs.get('length', 0)
        self.width = kwargs.get('width', 0)

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    dimensions = {'length': 15, 'width': 7}
    rect = Rectangle(**dimensions)
    print(rect.get_perimeter())