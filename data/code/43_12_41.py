class Square:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def validate_side_length(side_length):
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")

    def __init__(self, side_length):
        Square.validate_side_length(side_length)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [
        Square(3),
        Square(7),
        Square(10)
    ]
    for square in sample_squares:
        print(f"The area of a square with side length {square.side_length} is {square.area()}")