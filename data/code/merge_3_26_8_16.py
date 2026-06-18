import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """
    Determines if `a` is strictly greater than `b`.
    
    Args:
        a (int|float): The first number to compare.
        b (int|float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(3, 5))
    
    def test_floats(self):
        self.assertTrue(check_comparison(1.5, 0.9))
        self.assertFalse(check_comparison(-2.3, -4.7))

    def test_equality(self):
        # Equality should return False since the condition is strictly greater than (>)
        self.assertFalse(check_comparison(10, 10))
    
    def test_negative_numbers(self):
        # Negative numbers where first is larger (closer to zero)
        self.assertTrue(check_comparison(-5, -20))
        # Negative numbers where second is larger
        self.assertFalse(check_comparison(-20, -5))

    def test_zero_cases(self):
        self.assertFalse(check_comparison(0, 1))
        self.assertTrue(check_comparison(1, 0))

if __name__ == '__main__':
    unittest.main()