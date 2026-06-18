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
        self.assertFalse(check_comparison(4, 5))
        
    def test_negative_numbers(self):
        # -1 is greater than -2
        self.assertTrue(check_comparison(-1, -2))
        # Positive number should be greater than negative
        self.assertTrue(check_comparison(0, -5))
        self.assertFalse(check_comparison(-3, 4))
        
    def test_float_numbers(self):
        self.assertTrue(check_comparison(1.79, 1.78))
        self.assertFalse(check_comparison(2.00, 2.01))
        
    def test_edge_case_equality(self):
        # Equality should return False as per strict greater than logic
        self.assertFalse(check_comparison(5, 5))
        self.assertFalse(check_comparison(-10.0, -10.0))
        self.assertTrue(not check_comparison(3.0, 3.0))
        
    def test_edge_case_zero(self):
        # Zero vs positive/negative integers and floats
        self.assertEqual(check_comparison(0, -5), True)
        self.assertFalse(check_comparison(-5, 0))
        self.assertFalse(check_comparison(1, 0))

if __name__ == '__main__':
    unittest.main()