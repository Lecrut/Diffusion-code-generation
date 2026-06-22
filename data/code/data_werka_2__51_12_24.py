class Square:
    DEFAULT_SIDE_LENGTH = 10

    @staticmethod
    def calculate_perimeter(side_length):
        return 4 * side_length

    def __init__(self, side_length=DEFAULT_SIDE_LENGTH):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

if __name__ == '__main__':
    sample_side_length = 9
    square = Square(sample_side_length)
    perimeter = Square.calculate_perimeter(square.side_length)
    print(perimeter)