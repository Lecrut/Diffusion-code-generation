class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        if side_length <= self.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self._compute_area()

    def _compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = {
        'tiny': 1,
        'standard': 6,
        'giant': 15
    }
    for description, length in sample_side_lengths.items():
        try:
            square = Square(length)
            print(f"The area of a {description} square with side length {length} is: {square.area()}")
        except ValueError as e:
            print(e)