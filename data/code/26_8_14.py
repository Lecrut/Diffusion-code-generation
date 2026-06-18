import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

class TestCheckComparison(unittest.TestCase):
    def test_positive_integers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 4))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-1, -5))
        self.assertFalse(check_comparison(-2, -1))

    def test_floats(self):
        self.assertTrue(check_comparison(3.5, 3.0))
        self.assertFalse(check_comparison(3.0, 3.5))
        self.assertEqual(float('inf'), float('inf'))  # Just to ensure no crash on inf comparison logic if it existed

    def test_zero_and_negatives(self):
        self.assertTrue(check_comparison(-1, -2))
        self.assertFalse(check_comparison(0, 0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)