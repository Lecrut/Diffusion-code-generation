class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(square.area())
    another_square = Square(7)
    print(another_square.area())