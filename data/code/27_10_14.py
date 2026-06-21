import math

class TriangleValidator:
    EPSILON = 1e-9

    @staticmethod
    def is_valid(sides):
        if len(sides) != 3:
            return False
        a, b, c = sorted(sides)
        if a <= 0:
            return False
        return a + b > c + TriangleValidator.EPSILON

if __name__ == '__main__':
    print(TriangleValidator.is_valid((3.0, 4.0, 5.0)))
    print(TriangleValidator.is_valid((1.0, 1.0, 2.0)))
    print(TriangleValidator.is_valid((0.1, 0.2, 0.3)))
    print(TriangleValidator.is_valid((10.0, 5.0, 2.0)))
    print(TriangleValidator.is_valid((-5.0, 5.0, 10.0)))