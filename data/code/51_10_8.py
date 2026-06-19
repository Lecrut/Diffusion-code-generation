class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def is_valid(self):
        if not all(isinstance(side, (int, float)) and side > 0 for side in self.sides):
            return False
        return True

    def calculate_perimeter(self):
        if not self.is_valid():
            raise ValueError("Invalid polygon sides")
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [5, 7, 8, 10]
    polygon = Polygon(sample_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)