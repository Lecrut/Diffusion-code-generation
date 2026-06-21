class Shape:
    def __init__(self, side_length):
        self.side = side_length

    def get_area(self):
        if self.side is None:
            return 0
        return self.side ** 2

if __name__ == '__main__':
    shape = Shape(side_length=10)
    print(shape.get_area())