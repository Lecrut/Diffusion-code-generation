class Square:
    def __init__(self, side_length):
        if not self.is_valid_side_length(side_length):
            raise ValueError("Side length must be a positive number")
        self.side_length = side_length

    @staticmethod
    def is_valid_side_length(side_length):
        return isinstance(side_length, (int, float)) and side_length > 0

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side_length = 6.0
    square = Square(sample_side_length)
    print(square.area())