import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """
    Determines if a is strictly greater than b.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):
    
    def test_positive_integers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 4))
        
    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-1, -5))
        self.assertFalse(check_comparison(-2, -2))
        
    def test_floats(self):
        self.assertTrue(check_comparison(3.14, 3.0))
        self.assertFalse(check_comparison(3.0, 3.14))
        
    def test_zero_and_negatives(self):
        self.assertTrue(check_comparison(0, -5))
        self.assertFalse(check_comparison(-5, 0))

if __name__ == '__main__':
    unittest.main()