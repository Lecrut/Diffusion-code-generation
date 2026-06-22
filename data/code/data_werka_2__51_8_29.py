class Polygon:
    def __init__(self, side_lengths):
        self._validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def _validate_side_lengths(self, side_lengths):
        if not isinstance(side_lengths, list) or len(side_lengths) < 3:
            raise ValueError('Side lengths must be provided as a list with at least three elements.')
        for length in side_lengths:
            if not isinstance(length, (int, float)) or length <= 0:
                raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_values = [6, 8, 10]
    polygon = Polygon(sample_values)
    print(polygon.perimeter())