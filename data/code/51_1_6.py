class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_sides = [10, 20, 30, 40]
    polygon = Polygon(sample_sides)
    print(polygon.perimeter())