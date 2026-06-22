class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    side_length = 9
    square = Square(side_length)
    print(square.perimeter())