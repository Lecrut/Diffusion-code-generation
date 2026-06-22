class Polygon:
    MIN_SIDES = 3

    @staticmethod
    def validate_side_lengths(side_lengths):
        if not isinstance(side_lengths, list):
            raise TypeError('Input must be a list of side lengths.')
        if any((not isinstance(side, (int, float)) for side in side_lengths)):
            raise ValueError('All elements in the list must be numbers.')
        if len(side_lengths) < Polygon.MIN_SIDES:
            raise ValueError(f'A polygon must have at least {Polygon.MIN_SIDES} sides.')

    def __init__(self, side_lengths):
        Polygon.validate_side_lengths(side_lengths)
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_polygons = [
        [3, 4, 5],
        [10, 10, 10, 10],
        [6, 7, 8, 9, 10]
    ]
    
    for sides in sample_polygons:
        try:
            polygon = Polygon(sides)
            perimeter = polygon.calculate_perimeter()
            print(f"The perimeter of the polygon with sides {sides} is: {perimeter}")
        except Exception as e:
            print(e)

    empty_polygon = Polygon([])
    print(empty_polygon.calculate_perimeter())