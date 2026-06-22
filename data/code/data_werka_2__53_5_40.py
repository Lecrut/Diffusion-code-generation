class Square:
    def __init__(self, side_length):
        self._validate_side_length(side_length)
        self.side_length = side_length

    def _validate_side_length(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length <= 0:
            raise ValueError("Side length must be positive")

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side_lengths = [6, 8.2, 12]
    for length in sample_side_lengths:
        try:
            square = Square(length)
            area_result = square.area()
            print(f"The area of a square with side length {length} is: {area_result}")
        except (TypeError, ValueError) as e:
            print(e)