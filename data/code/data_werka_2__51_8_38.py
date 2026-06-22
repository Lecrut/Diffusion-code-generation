class Polygon:

    def __init__(self, side_lengths):
        if not all((isinstance(length, (int, float)) and length > 0 for length in side_lengths)):
            raise ValueError('All side lengths must be positive numbers.')
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)
if __name__ == '__main__':
    triangle_sides = [3, 4, 5]
    square_sides = [4, 4, 4, 4]
    triangle = Polygon(triangle_sides)
    square = Polygon(square_sides)
    print('Triangle perimeter:', triangle.perimeter())
    print('Square perimeter:', square.perimeter())