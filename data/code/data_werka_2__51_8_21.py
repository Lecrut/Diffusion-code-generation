class Polygon:
    def __init__(self, side_lengths):
        self.validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def validate_side_lengths(self, side_lengths):
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_values = [7, 10, 5]
    polygon = Polygon(sample_values)
    print(polygon.perimeter())