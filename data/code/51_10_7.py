class Polygon:

    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    sample_sides_1 = [3, 4, 5]
    sample_polygon_1 = Polygon(sample_sides_1)
    print('Perimeter of polygon 1:', sample_polygon_1.calculate_perimeter())
    sample_sides_2 = [7, 9, 10, 8]
    sample_polygon_2 = Polygon(sample_sides_2)
    print('Perimeter of polygon 2:', sample_polygon_2.calculate_perimeter())