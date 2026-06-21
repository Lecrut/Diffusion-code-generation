class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length must be non-negative")
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(square.calculate_area())

    square_large = Square(10)
    print(square_large.calculate_area())

    square_zero = Square(0)
    print(square_zero.calculate_area())