class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
        self._validate_side_lengths()

    def _validate_side_lengths(self):
        if not all(isinstance(length, (int, float)) and length > 0 for length in self.side_lengths):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_sides = [6, 8, 10]
    polygon = Polygon(sample_sides)
    print(polygon.perimeter())