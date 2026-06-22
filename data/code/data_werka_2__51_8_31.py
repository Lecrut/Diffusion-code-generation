class Polygon:
    def __init__(self, side_lengths):
        self.validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def validate_side_lengths(self, side_lengths):
        if not isinstance(side_lengths, list) or not side_lengths:
            raise ValueError('Side lengths must be a non-empty list.')
        for length in side_lengths:
            if not isinstance(length, (int, float)) or length <= 0:
                raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        polygon = Polygon([6, 8, 10])
        print(polygon.perimeter())
    except ValueError as e:
        print(e)