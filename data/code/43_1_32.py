class Square:
    DEFAULT_SIDE_LENGTH = 5

    def __init__(self, side_length=None):
        if side_length is None:
            self.side_length = Square.DEFAULT_SIDE_LENGTH
        else:
            self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

    def area(self):
        return Square.calculate_area(self.side_length)

if __name__ == '__main__':
    sample_side_length = 5
    square = Square(sample_side_length)
    print(square.area())