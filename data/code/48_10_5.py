class TriangleValidator:
    MIN_VALID_SIDE = 1

    @staticmethod
    def is_valid_triangle(sides):
        if len(sides) != 3:
            return False
        sorted_sides = sorted(sides)
        a, b, c = sorted_sides
        return a >= TriangleValidator.MIN_VALID_SIDE and b >= TriangleValidator.MIN_VALID_SIDE and c >= TriangleValidator.MIN_VALID_SIDE and a + b > c

if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 4]]
    for sides in sample_values:
        print(TriangleValidator.is_valid_triangle(sides))