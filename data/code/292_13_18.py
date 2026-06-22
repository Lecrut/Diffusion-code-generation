class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    polygon = Polygon([3, 4, 5])
    print(polygon.perimeter())