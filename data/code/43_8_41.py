class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

if __name__ == '__main__':
    square_side = 5
    square = Square(square_side)
    print(square.area())