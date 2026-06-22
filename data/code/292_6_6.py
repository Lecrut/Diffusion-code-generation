class IrregularPolygon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    polygon_sides = [5, 3, 4, 2]
    polygon = IrregularPolygon(polygon_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)