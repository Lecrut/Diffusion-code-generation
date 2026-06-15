import unittest
def calculate_difference(a, b):
    return a - b
class TestDifferenceCalculator(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_difference(10, 5), 5)
        self.assertEqual(calculate_difference(20, 8), 12)
    def test_negative_numbers(self):
        self.assertEqual(calculate_difference(-10, -5), -5)
        self.assertEqual(calculate_difference(-10, -2), -8)
        self.assertEqual(calculate_difference(5, -10), 15)
    def test_mixed_signs(self):
        self.assertEqual(calculate_difference(10, -5), 15)
        self.assertEqual(calculate_difference(-10, 5), -15)
        self.assertEqual(calculate_difference(-10, -5), -5)
    def test_zero_involvement(self):
        self.assertEqual(calculate_difference(5, 0), 5)
        self.assertEqual(calculate_difference(0, 5), -5)
        self.assertEqual(calculate_difference(0, 0), 0)
    def test_identical_numbers(self):
        self.assertEqual(calculate_difference(7, 7), 0)
        self.assertEqual(calculate_difference(-3, -3), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)