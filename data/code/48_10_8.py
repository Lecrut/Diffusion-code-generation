class TriangleValidator:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError("Input must contain exactly three side lengths.")
        self.sides = sorted(sides)

    def is_valid(self):
        a, b, c = self.sides
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [0, 4, 5],
        [-1, 4, 5],
        [5, 5, 5],
        [2, 2, 4]
    ]
    for sides in sample_values:
        try:
            validator = TriangleValidator(sides)
            print(validator.is_valid())
        except ValueError as e:
            print(e)