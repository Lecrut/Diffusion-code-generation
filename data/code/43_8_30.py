class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    SAMPLE_SIDE_LENGTH = 3
    square = Square(SAMPLE_SIDE_LENGTH)
    print(f"The area of the square with side length {SAMPLE_SIDE_LENGTH} is: {square.area()}")