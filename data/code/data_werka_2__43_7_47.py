class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        if side_length < self.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    @staticmethod
    def validate_side_length(side_length):
        return isinstance(side_length, (int, float)) and side_length >= Square.MIN_SIDE_LENGTH

    def area(self):
        if not Square.validate_side_length(self.side_length):
            raise ValueError("Invalid side length for area calculation")
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square = Square(8)
        print(f"The area of the square with side length {square.side_length} is: {square.area()}")
    except ValueError as e:
        print(e)