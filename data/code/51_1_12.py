class Polygon:

    def __init__(self, side_lengths):
        if not all((isinstance(length, (int, float)) and length > 0 for length in side_lengths)):
            raise ValueError('All side lengths must be positive numbers.')
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

    def add_side(self, length):
        if length > 0:
            self.side_lengths.append(length)
        else:
            raise ValueError('Side length must be a positive number.')
if __name__ == '__main__':
    try:
        sample_sides = [10, 20, 30]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
        polygon.add_side(40)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)