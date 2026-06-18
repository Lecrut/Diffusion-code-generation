import unittest

def check_comparison(a: float, b: float) -> bool:
    """
    Determines if a is strictly greater than b.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 4))
        self.assertFalse(check_comparison(2, 6))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-1, -5))
        self.assertFalse(check_comparison(-1, -1))
        self.assertFalse(check_comparison(-3, -7))

    def test_zero_and_mixed_signs(self):
        self.assertTrue(check_comparison(0, -1))
        self.assertFalse(check_comparison(0, 0))
        self.assertFalse(check_comparison(-5, 0))

if __name__ == '__main__':
    # Run tests with hard-coded sample values to ensure no external input is needed
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)