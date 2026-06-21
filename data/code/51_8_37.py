class Polygon:
    MIN_SIDES = 3

    def __init__(self, side_lengths):
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError('All side lengths must be positive numbers.')
        if len(side_lengths) < Polygon.MIN_SIDES:
            raise ValueError(f'A polygon must have at least {Polygon.MIN_SIDES} sides.')
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_values = [6, 8, 10]
    polygon = Polygon(sample_values)
    print(polygon.perimeter())