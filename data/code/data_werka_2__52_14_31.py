class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        self.validate_side_length()

    def validate_side_length(self):
        if not isinstance(self.side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4
    square = Square(sample_side_length)
    print(square.get_area())

    another_sample_side_length = 10
    another_square = Square(another_sample_side_length)
    print(another_square.get_area())