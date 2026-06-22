class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not all(isinstance(side, (int, float)) and side > 0 for side in self.sides):
            raise ValueError("All sides must be positive numbers.")
        if not self._is_valid_triangle():
            raise ValueError("The given sides do not form a valid triangle.")

    def _is_valid_triangle(self):
        return all(
            self.sides[i] + self.sides[j] > self.sides[k]
            for i, j, k in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
        )

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
        print(f'Side 1: {triangle.sides[0]}, Side 2: {triangle.sides[1]}, Side 3: {triangle.sides[2]}')
    except ValueError as e:
        print(e)