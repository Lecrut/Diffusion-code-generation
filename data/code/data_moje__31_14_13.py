class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

if __name__ == '__main__':
    sample_side = 50
    shape = Square(sample_side)
    print(shape.get_area())
    print(shape.get_perimeter())