class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    sample_side = 7
    square = Square(sample_side)
    print(square.area())