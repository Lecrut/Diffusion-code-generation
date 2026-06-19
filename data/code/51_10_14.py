class Polygon:

    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)
if __name__ == '__main__':
    triangle = Polygon([3, 4, 5])
    print(triangle.perimeter())