class Polygon:
    def __init__(self, sides):
        if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
            raise ValueError("All sides must be positive numbers.")
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        sample_sides = [3, 4, 5, 6]
        polygon = Polygon(sample_sides)
        print(polygon.perimeter())
    except ValueError as e:
        print(e)