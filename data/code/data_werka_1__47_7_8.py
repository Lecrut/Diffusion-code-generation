class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    shape1 = Shape(9, 4)
    print(shape1.area)
    shape2 = Shape(11, 6)
    print(shape2.area)