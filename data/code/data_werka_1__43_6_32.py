class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square1 = Square(5)
    print(square1.area())

    square2 = Square(0)
    print(square2.area())

    square3 = Square(2.5)
    print(square3.area())

    square4 = Square(100)
    print(square4.area())