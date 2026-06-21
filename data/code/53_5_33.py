class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        self._validate_side_length()

    def _validate_side_length(self):
        if not isinstance(self.side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if self.side_length <= 0:
            raise ValueError("Side length must be positive")

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [Square(3), Square(5.5), Square(7)]
    for square in sample_squares:
        print(f"The area of a square with side length {square.side_length} is: {square.area()}")