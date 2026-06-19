class TriangleValidator:
    def __init__(self, sides):
        self.sides = sorted(sides)

    def validate_sides(self):
        if len(self.sides) != 3:
            raise ValueError("Exactly three side lengths are required.")
        for side in self.sides:
            if side <= 0:
                raise ValueError("Side lengths must be positive.")

    def is_valid_triangle(self):
        try:
            self.validate_sides()
            a, b, c = self.sides
            return a + b > c
        except ValueError as e:
            print(f"Invalid input: {e}")
            return False

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5],
        [5, 5, 5], [2, 2, 4], [7, 10, 5], [8, 15, 17],
        [0, 9, 12], [-3, 6, 9], [4, 4, 4], [3, 3, 6]
    ]
    for sides in sample_values:
        validator = TriangleValidator(sides)
        print(validator.is_valid_triangle())