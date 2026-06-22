class Polygon:

    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    polygon1 = Polygon([3, 4, 5])
    print(polygon1.perimeter())
    polygon2 = Polygon([7, 8, 9, 10])
    print(polygon2.perimeter())
    empty_polygon = Polygon([])
    print(empty_polygon.perimeter())