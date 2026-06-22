class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 7
    square = Square(sample_side_length)
    print(square.area())