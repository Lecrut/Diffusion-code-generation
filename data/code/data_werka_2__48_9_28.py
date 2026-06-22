class TriangleValidator:
    def __init__(self, sides):
        self.sides = sides

    def is_valid(self):
        if len(self.sides) != 3:
            return False
        a, b, c = self.sides
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return self._triangle_inequality(a, b, c)

    def _triangle_inequality(self, a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [0, 4, 5],
        [-1, 4, 5],
        [5, 5, 5]
    ]
    for sides in sample_values:
        validator = TriangleValidator(sides)
        print(validator.is_valid())