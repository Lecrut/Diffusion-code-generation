class TriangleValidator:
    MIN_SIDES = 3

    @staticmethod
    def is_positive(sides):
        return all(side > 0 for side in sides)

    @staticmethod
    def satisfies_triangle_inequality(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def validate(self, sides):
        if len(sides) != TriangleValidator.MIN_SIDES:
            return False
        if not TriangleValidator.is_positive(sides):
            return False
        a, b, c = sorted(sides)
        return TriangleValidator.satisfies_triangle_inequality(a, b, c)

if __name__ == '__main__':
    validator = TriangleValidator()
    sample_values = [
        [3, 4, 5], 
        [1, 2, 3], 
        [0, 4, 5], 
        [-1, 4, 5], 
        [5, 5, 5], 
        [2, 2, 4],
        [7, 10, 5], 
        [8, 15, 17], 
        [0, 9, 12], 
        [-3, 6, 9], 
        [4, 4, 4], 
        [3, 3, 6]
    ]
    for sides in sample_values:
        print(validator.validate(sides))