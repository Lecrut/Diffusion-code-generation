class Polygon:

    def __init__(self, side_lengths):
        self.validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def validate_side_lengths(self, side_lengths):
        if not all((isinstance(length, (int, float)) and length > 0 for length in side_lengths)):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)
if __name__ == '__main__':
    triangle_sides = [3, 4, 5]
    rectangle_sides = [6, 8]
    hexagon_sides = [2] * 6
    triangle = Polygon(triangle_sides)
    rectangle = Polygon(rectangle_sides)
    hexagon = Polygon(hexagon_sides)
    print('Triangle perimeter:', triangle.perimeter())
    print('Rectangle perimeter:', rectangle.perimeter())
    print('Hexagon perimeter:', hexagon.perimeter())