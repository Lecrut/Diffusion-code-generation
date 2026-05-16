import unittest
class TriangleCalculator:
    def calculate_perimeter(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
            return None
        return a + b + c
class TestTriangleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = TriangleCalculator()
    def test_valid_triangle(self):
        result = self.calculator.calculate_perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    def test_valid_triangle_different_sides(self):
        result = self.calculator.calculate_perimeter(5, 12, 13)
        self.assertEqual(result, 30)
    def test_invalid_triangle_sum_too_small(self):
        result = self.calculator.calculate_perimeter(1, 2, 4)
        self.assertIsNone(result)
    def test_invalid_triangle_sum_too_large(self):
        result = self.calculator.calculate_perimeter(1, 2, 10)
        self.assertIsNone(result)
    def test_invalid_triangle_zero_side(self):
        result = self.calculator.calculate_perimeter(0, 4, 5)
        self.assertIsNone(result)
    def test_invalid_triangle_negative_side(self):
        result = self.calculator.calculate_perimeter(3, -4, 5)
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)