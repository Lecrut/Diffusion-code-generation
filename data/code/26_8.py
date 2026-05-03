import unittest
def check_comparison(a, b):
    return a > b
class TestCheckComparison(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(3, 5))
        self.assertFalse(check_comparison(5, 5))
    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-1, -5))
        self.assertFalse(check_comparison(-5, -1))
        self.assertFalse(check_comparison(-5, -5))
    def test_mixed_numbers(self):
        self.assertTrue(check_comparison(10, -2))
        self.assertFalse(check_comparison(-10, 2))
        self.assertTrue(check_comparison(-1, 0))
        self.assertFalse(check_comparison(0, -1))
    def test_equality(self):
        self.assertFalse(check_comparison(7, 7))
        self.assertFalse(check_comparison(0, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)