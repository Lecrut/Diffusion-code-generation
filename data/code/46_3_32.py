class Triangle:
    def __init__(self, side1, side2, side3):
        if not all(isinstance(side, int) and side > 0 for side in (side1, side2, side3)):
            raise ValueError("All sides must be positive integers.")
        self.sides = [side1, side2, side3]

    def perimeter(self):
        return sum(self.sides)

    def longest_side(self):
        return max(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 9, 5)
        print(triangle.perimeter())
        print(triangle.longest_side())
    except ValueError as e:
        print(e)