class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    polygon_sides = [3, 4, 5]
    polygon = Polygon(polygon_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)