class Polygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    @staticmethod
    def calculate_perimeter(num_sides, side_length):
        if num_sides < 3:
            raise ValueError("Number of sides must be at least 3")
        return num_sides * side_length

if __name__ == '__main__':
    polygon = Polygon(5, 3)
    perimeter = Polygon.calculate_perimeter(polygon.num_sides, polygon.side_length)
    print(f"Number of sides: {polygon.num_sides}")
    print(f"Side length: {polygon.side_length}")
    print(f"Perimeter: {perimeter}")