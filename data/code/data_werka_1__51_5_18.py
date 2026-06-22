class Polygon:

    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    polygon1 = Polygon([3, 4, 5])
    print(polygon1.calculate_perimeter())
    polygon2 = Polygon([10, 20, 30, 40])
    print(polygon2.calculate_perimeter())
    empty_polygon = Polygon([])
    print(empty_polygon.calculate_perimeter())