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
    sample_polygons = {
        'triangle': [3, 4, 5],
        'square': [4, 4, 4, 4],
        'pentagon': [5, 5, 5, 5, 5]
    }

    for name, sides in sample_polygons.items():
        polygon = Polygon(sides)
        print(f'{name.capitalize()} perimeter: {polygon.perimeter()}')