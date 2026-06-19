class Square:
    def __init__(self, side_length):
        self.validate_side_length(side_length)
        self.side_length = side_length

    def validate_side_length(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length <= 0:
            raise ValueError("Side length must be positive")

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    try:
        square = Square(8)
        print(square.perimeter())
    except (TypeError, ValueError) as e:
        print(e)