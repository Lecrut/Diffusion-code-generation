import unittest
class TestNumberComparison(unittest.TestCase):
    def compare_numbers(self, a, b):
        return a == b
    def test_equal_numbers(self):
        self.assertTrue(self.compare_numbers(5, 5))
        self.assertTrue(self.compare_numbers(0, 0))
        self.assertTrue(self.compare_numbers(-10, -10))
    def test_unequal_numbers(self):
        self.assertFalse(self.compare_numbers(5, 6))
        self.assertFalse(self.compare_numbers(1, 2))
        self.assertFalse(self.compare_numbers(-5, 5))
    def test_zero_involvement(self):
        self.assertTrue(self.compare_numbers(0, 5))
        self.assertTrue(self.compare_numbers(5, 0))
        self.assertTrue(self.compare_numbers(0, -0))
    def test_negative_numbers(self):
        self.assertTrue(self.compare_numbers(-5, -5))
        self.assertFalse(self.compare_numbers(-5, -4))
        self.assertFalse(self.compare_numbers(-1, -10))
    def test_mixed_signs(self):
        self.assertFalse(self.compare_numbers(5, -5))
        self.assertFalse(self.compare_numbers(-5, 5))
        self.assertFalse(self.compare_numbers(10, -10))
    def test_very_small_differences(self):
        self.assertTrue(self.compare_numbers(0.0, 0.000000000000001))
        self.assertFalse(self.compare_numbers(0.1, 0.100000000000001))
        self.assertFalse(self.compare_numbers(1.0, 1.0 + 1e-15))
    def test_floating_point_precision(self):
        self.assertTrue(self.compare_numbers(0.1 + 0.2, 0.3))
        self.assertFalse(self.compare_numbers(0.1 + 0.2, 0.3000000000000001))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)