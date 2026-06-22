class Polygon:
    MAX_SIDES = 10

    def __init__(self, side_lengths):
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError("All side lengths must be positive numbers.")
        if len(side_lengths) > self.MAX_SIDES:
            raise ValueError(f"Number of sides cannot exceed {self.MAX_SIDES}.")
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        sample_sides = [10, 20, 30, 40, 50]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)