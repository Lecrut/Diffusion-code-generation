import unittest

class Triangle:
    MAX_SIDE_LENGTH = 1000
    
    @staticmethod
    def validate_sides(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Side lengths must be positive")
        if a > Triangle.MAX_SIDE_LENGTH or b > Triangle.MAX_SIDE_LENGTH or c > Triangle.MAX_SIDE_LENGTH:
            raise ValueError("Side lengths exceed the maximum allowed length")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")

    @staticmethod
    def calculate_perimeter(a, b, c):
        Triangle.validate_sides(a, b, c)
        return a + b + c

class TestTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(Triangle.calculate_perimeter(3, 4, 5), 12)

    def test_equilateral_triangle(self):
        self.assertEqual(Triangle.calculate_perimeter(5, 5, 5), 15)

    def test_isosceles_triangle(self):
        self.assertEqual(Triangle.calculate_perimeter(5, 5, 8), 18)

    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(0, 4, 5)

    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(-3, 4, 5)

    def test_invalid_triangle_large_side(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(Triangle.MAX_SIDE_LENGTH + 1, 4, 5)

    def test_invalid_triangle_not_a_triangle(self):
        with self.assertRaises(ValueError):
            Triangle.calculate_perimeter(1, 2, 3)

if __name__ == '__main__':
    side_a = 6
    side_b = 8
    side_c = 10
    perimeter = Triangle.calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)