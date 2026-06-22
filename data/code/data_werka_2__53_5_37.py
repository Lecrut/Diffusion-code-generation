class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        if not isinstance(self.side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if self.side_length <= 0:
            raise ValueError("Side length must be positive")

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    test_side_lengths = [3, 6.5, 9]
    for length in test_side_lengths:
        try:
            square = Square(length)
            print(f"The area of a square with side length {length} is: {square.area()}")
        except (TypeError, ValueError) as e:
            print(e)