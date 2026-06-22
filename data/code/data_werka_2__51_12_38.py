class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def perimeter(self):
        return self._calculate_perimeter()

    def _calculate_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    sample_side_length = 9
    square = Square(sample_side_length)
    calculated_perimeter = square.perimeter()
    print(calculated_perimeter)