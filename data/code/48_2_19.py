class TriangleChecker:
    def __init__(self, sides):
        self.sides = sorted(sides)

    def is_valid_triangle(self):
        a, b, c = self.sides
        return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [10, 1, 1]
    ]
    for sides in sample_values:
        triangle_checker = TriangleChecker(sides)
        print(triangle_checker.is_valid_triangle())