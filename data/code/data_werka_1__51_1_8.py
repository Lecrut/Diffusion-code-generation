class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_sides_1 = [3, 4, 5]
    polygon1 = Polygon(sample_sides_1)
    print("Perimeter of polygon1:", polygon1.perimeter())

    sample_sides_2 = [7, 8, 9, 10]
    polygon2 = Polygon(sample_sides_2)
    print("Perimeter of polygon2:", polygon2.perimeter())