import unittest
class TestMathFunctions(unittest.TestCase):
    def sum_numbers(self, a, b):
        return a + b
    def test_sum_positive_numbers(self):
        self.assertEqual(self.sum_numbers(5, 3), 8)
    def test_sum_negative_numbers(self):
        self.assertEqual(self.sum_numbers(-5, -3), -8)
    def test_sum_positive_and_negative(self):
        self.assertEqual(self.sum_numbers(10, -4), 6)
    def test_sum_with_zero(self):
        self.assertEqual(self.sum_numbers(7, 0), 7)
    def test_sum_with_zero_negative(self):
        self.assertEqual(self.sum_numbers(-2, 0), -2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)