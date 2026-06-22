class IrregularPolygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    polygon_sides = [5, 3, 4, 2]
    polygon = IrregularPolygon(polygon_sides)
    print(polygon.perimeter())