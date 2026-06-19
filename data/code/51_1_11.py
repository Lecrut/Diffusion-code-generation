class Polygon:
    def __init__(self, side_lengths):
        if not isinstance(side_lengths, list) or not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError("Input must be a list of positive numbers.")
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    try:
        sample_sides = [10, 20, 30, 40]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)