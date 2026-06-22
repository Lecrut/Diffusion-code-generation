class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    polygon = Polygon(sample_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)