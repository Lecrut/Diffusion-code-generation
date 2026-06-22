class Polygon:
    def __init__(self, sides):
        if not isinstance(sides, list) or len(sides) < 3:
            raise ValueError("Sides must be a list with at least three elements.")
        if any(side <= 0 for side in sides):
            raise ValueError("All side lengths must be positive numbers.")
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [6, 9, 12, 15]
    polygon = Polygon(sample_sides)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)