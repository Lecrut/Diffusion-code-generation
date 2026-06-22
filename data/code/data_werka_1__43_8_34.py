class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH = 6
    square = Square(DEFAULT_SIDE_LENGTH)
    print(f"The area of the square with side length {DEFAULT_SIDE_LENGTH} is: {square.area()}")