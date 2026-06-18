import unittest

def check_comparison(a: float, b: float) -> bool:
    """Returns True if a is strictly greater than b."""
    return a > b

class TestCheckComparison(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 5))

    def test_negative_numbers(self):
        # -1 is not greater than -2 (since -1 > -2) -> True
        self.assertTrue(check_comparison(-1, -2))
        # -5 is less than -6? No. -5 > -6 -> True
        self.assertFalse(check_comparison(-3, -4))  # -3 < -4 is False

    def test_equality(self):
        # Equal values should not satisfy strict inequality
        self.assertFalse(check_comparison(7, 7))
        self.assertFalse(check_comparison(0.5, 0.5))

    def test_boundary_zero(self):
        self.assertTrue(check_comparison(1, 0))
        self.assertFalse(check_comparison(-1, 0))

if __name__ == '__main__':
    unittest.main()