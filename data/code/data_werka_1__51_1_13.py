class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = self.validate_side_lengths(side_lengths)

    def validate_side_lengths(self, side_lengths):
        if not isinstance(side_lengths, list):
            raise TypeError("Side lengths must be provided as a list.")
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError("All side lengths must be positive numbers.")
        return side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        sample_sides = [10, 20, 30, 40]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except (TypeError, ValueError) as e:
        print(e)