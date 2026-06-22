class Square:
    def __init__(self, side_length):
        if not self._validate_side_length(side_length):
            raise ValueError("Side length must be a non-negative number")
        self.side_length = side_length

    def _validate_side_length(self, side_length):
        return isinstance(side_length, (int, float)) and side_length >= 0

    def compute_area(self):
        return self._calculate_area(self.side_length)

    def _calculate_area(self, side_length):
        return side_length ** 2

if __name__ == '__main__':
    try:
        sample_square = Square(10)
        print(f"The area of the square is: {sample_square.compute_area()}")
    except ValueError as e:
        print(e)