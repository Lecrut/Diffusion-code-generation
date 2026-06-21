class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    @staticmethod
    def validate_side_length(side_length):
        if not isinstance(side_length, (int, float)) or side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be a non-negative number")

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square = Square(8)
        print(f"The area of the square is: {square.area()}")
    except ValueError as e:
        print(e)