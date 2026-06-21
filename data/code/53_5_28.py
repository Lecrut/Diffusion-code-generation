class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self._compute_area()

    def _compute_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side_length = 6
    try:
        square = Square(sample_side_length)
        result = square.area()
        print(f"The area of a square with side length {sample_side_length} is: {result}")
    except ValueError as e:
        print(e)