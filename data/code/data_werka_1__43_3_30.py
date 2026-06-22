class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square1 = Square(3)
    print(f"Area of square with side {square1.side_length}: {square1.area}")
    square2 = Square(4)
    print(f"Area of square with side {square2.side_length}: {square2.area}")