class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    polygon1 = Polygon([3, 4, 5])
    print(polygon1.calculate_perimeter())

    polygon2 = Polygon([6, 7, 8, 9])
    print(polygon2.calculate_perimeter())