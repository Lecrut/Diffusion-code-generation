class Polygon:
    MIN_SIDES = 3

    @staticmethod
    def calculate_perimeter(sides):
        if not sides or len(sides) < Polygon.MIN_SIDES:
            return None
        if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
            return None
        return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9, 10]
    perimeter = Polygon.calculate_perimeter(sample_sides)
    if perimeter is not None:
        print(f"The sides of the polygon are: {sample_sides}")
        print(f"The total perimeter is: {perimeter}")
    else:
        print("Error: Invalid input provided. Sides must be positive numbers and there must be at least three sides.")