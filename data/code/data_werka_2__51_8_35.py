class Polygon:
    def __init__(self, side_lengths):
        self._validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def _validate_side_lengths(self, side_lengths):
        if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    hexagon_sides = [6, 6, 6, 6, 6, 6]
    octagon_sides = [8, 8, 8, 8, 8, 8, 8, 8]
    polygon1 = Polygon(hexagon_sides)
    polygon2 = Polygon(octagon_sides)
    
    print('Hexagon perimeter:', polygon1.perimeter())
    print('Octagon perimeter:', polygon2.perimeter())