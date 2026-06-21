class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

if __name__ == '__main__':
    square_side = 7
    square = Square(square_side)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())