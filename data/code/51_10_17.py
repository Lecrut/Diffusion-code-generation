class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    SAMPLE_SIDES = [3, 4, 5]
    polygon = Polygon(SAMPLE_SIDES)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)