class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    @staticmethod
    def is_valid_triangle(sides):
        if len(sides) != 3:
            return False
        a, b, c = sorted(sides)
        return a + b > c

    def can_form_triangle(self):
        return TriangleChecker.is_valid_triangle(self.sides)

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [10, 1, 1]
    ]
    for sides in sample_values:
        triangle_checker = TriangleChecker(sides)
        print(triangle_checker.can_form_triangle())