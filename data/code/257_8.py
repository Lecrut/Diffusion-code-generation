import unittest
def calculate_difference(a, b):
    return a - b
class TestDifferenceCalculation(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_difference(10, 5), 5)
        self.assertEqual(calculate_difference(20, 8), 12)
    def test_negative_numbers(self):
        self.assertEqual(calculate_difference(-10, -5), -5)
        self.assertEqual(calculate_difference(-10, -2), -8)
        self.assertEqual(calculate_difference(-5, -10), 5)
    def test_mixed_signs(self):
        self.assertEqual(calculate_difference(10, -5), 15)
        self.assertEqual(calculate_difference(-10, 5), -15)
        self.assertEqual(calculate_difference(-10, -5), -5)
    def test_with_zero(self):
        self.assertEqual(calculate_difference(10, 0), 10)
        self.assertEqual(calculate_difference(0, 10), -10)
        self.assertEqual(calculate_difference(0, 0), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)