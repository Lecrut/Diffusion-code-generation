class Square:
    def __init__(self, side_length):
        self._set_side_length(side_length)

    def _set_side_length(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self._compute_area()

    def _compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [
        Square(3),
        Square(6.5),
        Square(9)
    ]
    for square in sample_squares:
        print(f"The area of a square with side length {square.side_length} is: {square.area()}")