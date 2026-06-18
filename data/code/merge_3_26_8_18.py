import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """
    Determines if `a` is strictly greater than `b`.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
        
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
        self.assertFalse(check_comparison(-5, -5))
        self.assertFalse(check_comparison(-3, -1))

    def test_mixed_signs(self):
        self.assertTrue(check_comparison(0, -1))
        self.assertFalse(check_comparison(-1, 0))
        self.assertTrue(check_comparison(float('inf'), float('-inf')))
        
    def test_float_precision_edge_cases(self):
        # Test very close numbers where precision matters
        a = 3.5
        b = 3.4999999999999996
        self.assertTrue(check_comparison(a, b))

        c = float('nan')
        d = float('-inf')
        # NaN comparisons always return False in Python's > operator for the first operand being greater than anything including -inf? 
        # Actually: nan > x is always False. So this test case expects False.
        self.assertFalse(check_comparison(c, d))

if __name__ == '__main__':
    unittest.main()