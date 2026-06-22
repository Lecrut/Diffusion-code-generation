class Polygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def calculate_perimeter(self):
        return self.num_sides * self.side_length

if __name__ == '__main__':
    polygon = Polygon(5, 3)
    print(f"Number of sides: {polygon.num_sides}")
    print(f"Side length: {polygon.side_length}")
    print(f"Perimeter: {polygon.calculate_perimeter()}")