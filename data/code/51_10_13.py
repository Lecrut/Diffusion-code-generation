class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample_sides = [3, 4, 5, 6]
    polygon = Polygon(sample_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)