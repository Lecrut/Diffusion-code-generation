class Polygon:

    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

    def add_side(self, length):
        if length > 0:
            self.side_lengths.append(length)
        else:
            raise ValueError('Side length must be a positive number.')
if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    polygon = Polygon(sample_sides)
    print(polygon.perimeter())
    try:
        polygon.add_side(6)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)
    invalid_side = -2
    try:
        polygon.add_side(invalid_side)
    except ValueError as e:
        print(e)