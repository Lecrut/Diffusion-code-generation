class Square:
    def __init__(self, side_length):
        self._validate_side_length(side_length)
        self.side_length = side_length

    def _validate_side_length(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if side_length < 0:
            raise ValueError("Side length cannot be negative")

    def compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        sample_square = Square(5)
        print(f"The area of the square with side length {sample_square.side_length} is: {sample_square.compute_area()}")
    except ValueError as e:
        print(e)