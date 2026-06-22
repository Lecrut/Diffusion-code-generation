class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9]
    polygon = Polygon(sample_sides)
    print(polygon.perimeter())