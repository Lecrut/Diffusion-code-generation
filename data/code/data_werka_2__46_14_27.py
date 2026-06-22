class Triangle:
    def __init__(self, side_lengths):
        if len(side_lengths) != 3:
            raise ValueError("A triangle must have exactly three sides.")
        self.side_lengths = side_lengths
        self._validate_sides()

    def _validate_sides(self):
        for length in self.side_lengths:
            if length <= 0:
                raise ValueError("Side lengths must be positive numbers.")

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    side_lengths = {1: 4, 2: 5, 3: 6}
    triangle = Triangle(list(side_lengths.values()))
    print(triangle.perimeter())