class TriangleChecker:
    MIN_SIDES = 3

    @staticmethod
    def validate_sides(sides):
        if len(sides) != TriangleChecker.MIN_SIDES:
            return False
        for side in sides:
            if side <= 0:
                return False
        return True

    @staticmethod
    def satisfies_triangle_inequality(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @classmethod
    def can_form_triangle(cls, sides):
        if not cls.validate_sides(sides):
            return False
        a, b, c = sorted(sides)
        return cls.satisfies_triangle_inequality(a, b, c)

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 1, 2],
        [0, 1, 1],
        [-1, 1, 1],
        [5, 5, 5],
        [2, 2, 3],
        [7, 10, 5],
        [6, 6, 6],
        [8, 15, 17],
        [1, 1, 2],
        [0, 5, 5],
        [-3, 4, 5]
    ]
    for sides in sample_values:
        print(TriangleChecker.can_form_triangle(sides))