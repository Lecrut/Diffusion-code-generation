class Polygon:
    def __init__(self, sides):
        if not isinstance(sides, list) or len(sides) < 3:
            raise ValueError("Sides must be a list with at least three elements.")
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive numbers.")
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        sample_sides = [5, 7, 8, 10]
        polygon = Polygon(sample_sides)
        perimeter = polygon.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)