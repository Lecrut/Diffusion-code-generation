class Square:
    def __init__(self, side_length):
        self.side_length = self.validate_side_length(side_length)

    @staticmethod
    def validate_side_length(side_length):
        if not isinstance(side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return side_length

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4
    square = Square(sample_side_length)
    area = square.get_area()
    print(area)

    another_sample_side_length = 9
    another_square = Square(another_sample_side_length)
    another_area = another_square.get_area()
    print(another_area)