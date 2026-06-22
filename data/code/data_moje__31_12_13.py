class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side = 7
    square_instance = Square(sample_side)
    print(square_instance.area())