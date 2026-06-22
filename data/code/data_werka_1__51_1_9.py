class Polygon:
    def __init__(self, side_lengths):
        if not self._validate_sides(side_lengths):
            raise ValueError("Invalid side lengths provided.")
        self.side_lengths = side_lengths

    def _validate_sides(self, sides):
        return all(isinstance(length, (int, float)) and length > 0 for length in sides)

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        sample_sides = [10, 12, 15]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)