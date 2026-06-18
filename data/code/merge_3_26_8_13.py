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

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(2, 7))
        
    def test_negative_numbers(self):
        self.assertTrue(-10, -20)
        self.assertFalse(-5, -10)
        
    def test_zero_and_negatives(self):
        self.assertTrue(0, -5)
        self.assertFalse(-3, 0)
        
    def test_equality_cases(self):
        self.assertFalse(check_comparison(4, 4))
        self.assertFalse(check_comparison(-7.5, -7.5))
        
    def test_float_precision(self):
        self.assertTrue(float('inf'), float('-inf'))
        self.assertTrue(10.000000001, 10)

if __name__ == '__main__':
    unittest.main()