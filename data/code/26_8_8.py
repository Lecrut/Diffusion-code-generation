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

    def test_equal_numbers(self):
        self.assertFalse(check_comparison(5, 5))
        self.assertFalse(check_comparison(-10.5, -10.5))
    
    def test_positive_greater_than(self):
        self.assertTrue(check_comparison(10, 5))
        self.assertTrue(check_comparison(float('inf'), float('-inf')))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-2, -5))
        self.assertFalse(check_comparison(-5, -2))

    def test_float_precision_edge_cases(self):
        # Test floats that are very close but not equal to ensure > works correctly
        a = 1.0 + 1e-16
        b = 1.0
        self.assertTrue(a > b)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)