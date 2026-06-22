class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        if self.side < 0:
            raise ValueError("Side length cannot be negative")
        return self.side ** 2

if __name__ == '__main__':
    SQUARE_SIDE = 50
    shape = Square(SQUARE_SIDE)
    print(shape.area())