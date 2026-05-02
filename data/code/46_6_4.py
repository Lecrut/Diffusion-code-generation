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
        self.assertEqual(self.calculator.calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(self.calculator.calculate_perimeter(5, 12, 13), 30)
        self.assertEqual(self.calculator.calculate_perimeter(10, 10, 10), 30)
    def test_invalid_triangle_triangle_inequality(self):
        self.assertIsNone(self.calculator.calculate_perimeter(1, 2, 10))
        self.assertIsNone(self.calculator.calculate_perimeter(10, 1, 1))
        self.assertIsNone(self.calculator.calculate_perimeter(1, 1, 10))
    def test_invalid_triangle_zero_side(self):
        self.assertIsNone(self.calculator.calculate_perimeter(0, 4, 5))
        self.assertIsNone(self.calculator.calculate_perimeter(3, 0, 5))
        self.assertIsNone(self.calculator.calculate_perimeter(5, 0, 5))
    def test_invalid_triangle_negative_side(self):
        self.assertIsNone(self.calculator.calculate_perimeter(-1, 2, 3))
        self.assertIsNone(self.calculator.calculate_perimeter(3, -1, 4))
        self.assertIsNone(self.calculator.calculate_perimeter(5, 5, -1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)