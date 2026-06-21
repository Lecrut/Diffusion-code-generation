class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    sample_side_length = 6
    square = Square(sample_side_length)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())