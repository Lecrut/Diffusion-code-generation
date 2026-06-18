import unittest

def check_comparison(a: float, b: float) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

class TestCheckComparison(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5.0, 3.0))
        self.assertTrue(check_comparison(100.0, -99.0))

    def test_negative_numbers(self):
        self.assertFalse(check_comparison(-5.0, -2.0))  # False because -5 is not > -2
        self.assertTrue(check_comparison(-3.0, -7.0))   # True because -3 is greater than -7

    def test_equality(self):
        self.assertFalse(check_comparison(4.0, 4.0))     # Strict inequality fails on equality
        self.assertFalse(check_comparison("a", "a"))      # String comparison for edge case

    def test_zero_cases(self):
        self.assertTrue(check_comparison(1.0, 0.0))       # Positive vs zero
        self.assertFalse(check_comparison(0.0, 0.0))      # Zero equals itself

if __name__ == '__main__':
    unittest.main()