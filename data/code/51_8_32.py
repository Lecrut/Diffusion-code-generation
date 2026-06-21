class Polygon:

    def __init__(self, side_lengths):
        if not all((isinstance(length, (int, float)) and length > 0 for length in side_lengths)):
            raise ValueError('All side lengths must be positive numbers.')
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)
if __name__ == '__main__':
    triangle = Polygon([3, 4, 5])
    square = Polygon([10, 10, 10, 10])
    print('Triangle Perimeter:', triangle.perimeter())
    print('Square Perimeter:', square.perimeter())