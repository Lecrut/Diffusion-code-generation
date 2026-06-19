class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square1 = Square(5)
    print("Area of square1:", square1.area())

    square2 = Square(7)
    print("Area of square2:", square2.area())