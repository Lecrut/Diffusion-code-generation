class TriangleValidator:
    def __init__(self, sides):
        self.sides = sorted(sides)

    def is_valid(self):
        return self._all_sides_positive() and self._triangle_inequality()

    def _all_sides_positive(self):
        return all(side > 0 for side in self.sides)

    def _triangle_inequality(self):
        a, b, c = self.sides
        return a + b > c

if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 4]]
    for sides in sample_values:
        validator = TriangleValidator(sides)
        print(validator.is_valid())