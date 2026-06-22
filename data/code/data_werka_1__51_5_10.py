class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    polygon1 = Polygon([3, 4, 5])
    print(polygon1.calculate_perimeter())

    polygon2 = Polygon([6, 7, 8, 9])
    print(polygon2.calculate_perimeter())

    empty_polygon = Polygon([])
    print(empty_polygon.calculate_perimeter())