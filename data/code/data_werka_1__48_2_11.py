class TriangleChecker:
    TRIANGLE_SIDES = 3

    @staticmethod
    def is_valid_triangle(sides):
        if len(sides) != TriangleChecker.TRIANGLE_SIDES:
            return False
        a, b, c = sorted(sides)
        return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [10, 1, 1]
    ]
    for sides in sample_values:
        print(TriangleChecker.is_valid_triangle(sides))