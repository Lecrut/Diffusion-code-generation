class Polygon:
    MIN_SIDES = 3

    def __init__(self, side_lengths):
        if len(side_lengths) < self.MIN_SIDES:
            raise ValueError("A polygon must have at least 3 sides.")
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError("All side lengths must be positive numbers.")
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        sample_sides = [10, 12, 8]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)