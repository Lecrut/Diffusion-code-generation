class Polygon:
    def __init__(self, sides):
        if not all(isinstance(s, (int, float)) and s > 0 for s in sides):
            raise ValueError("All side lengths must be positive numbers.")
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [10, 20, 30, 40]
    polygon = Polygon(sample_sides)
    print(polygon.perimeter())