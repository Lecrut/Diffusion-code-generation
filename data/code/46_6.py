import unittest
class TriangleCalculator:
    def calculate_perimeter(self, a, b, c):
        if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
            return a + b + c
        else:
            return None
class TestTriangleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = TriangleCalculator()
    def test_valid_triangle(self):
        result = self.calculator.calculate_perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    def test_valid_triangle_different_sides(self):
        result = self.calculator.calculate_perimeter(5, 12, 13)
        self.assertEqual(result, 30)
    def test_invalid_triangle_sum_inequality(self):
        result = self.calculator.calculate_perimeter(1, 2, 10)
        self.assertIsNone(result)
    def test_invalid_triangle_zero_side(self):
        result = self.calculator.calculate_perimeter(0, 4, 5)
        self.assertIsNone(result)
    def test_invalid_triangle_negative_side(self):
        result = self.calculator.calculate_perimeter(3, -4, 5)
        self.assertIsNone(result)
    def test_invalid_triangle_degenerate(self):
        result = self.calculator.calculate_perimeter(1, 2, 3)
        self.assertEqual(result, 6)
    def test_invalid_triangle_degenerate_case(self):
        result = self.calculator.calculate_perimeter(1, 2, 3)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)