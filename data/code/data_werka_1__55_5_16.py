import unittest

class Triangle:
    MIN_SIDE_LENGTH = 0.1

    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        return (a > Triangle.MIN_SIDE_LENGTH and b > Triangle.MIN_SIDE_LENGTH and c > Triangle.MIN_SIDE_LENGTH and
                a + b > c and a + c > b and b + c > a)

    @staticmethod
    def calculate_perimeter(a: float, b: float, c: float) -> float:
        if not Triangle.is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle side lengths")
        return a + b + c

class TestTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(Triangle.calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(Triangle.calculate_perimeter(6, 8, 10), 24)

    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(0, 4, 5)

    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(-3, 4, 5)

    def test_invalid_triangle_not_a_triangle(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(1, 2, 3)

if __name__ == '__main__':
    side_a = 3.0
    side_b = 4.0
    side_c = 5.0
    perimeter = Triangle.calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)