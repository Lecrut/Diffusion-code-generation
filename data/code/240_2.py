class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    square1 = Square(5)
    print(square1.area())
    square2 = Square(10.5)
    print(square2.area())