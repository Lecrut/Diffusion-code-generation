class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    @property
    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length1 = 3
    sample_side_length2 = 8
    square1 = Square(sample_side_length1)
    square2 = Square(sample_side_length2)
    print(square1.area)
    print(square2.area)