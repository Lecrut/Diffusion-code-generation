class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    shape1 = Shape(4, 6)
    print(shape1.area())