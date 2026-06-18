import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """
    Determines if 'a' is strictly greater than 'b'.
    
    Args:
        a (int or float): The first value to compare.
        b (int or float): The second value to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(check_comparison(10, 5))
        self.assertFalse(check_comparison(5, 10))
        
    def test_negative_numbers(self):
        self.assertTrue(-2.5 > -5)
        self.assertFalse(-5 > -2.5)

    def test_zero_and_negatives(self):
        self.assertTrue(0 > -5)
        self.assertFalse(-5 > 0)

    def test_float_precision_edge_cases(self):
        # Test floats very close to each other but not equal
        a = 1.3333333333333333
        b = 4/3
        self.assertTrue(a == b, "Float comparison failed: {0} is not equal to {1}".format(a, b))

    def test_equality_cases(self):
        # Equality should return False for strict greater-than operator
        self.assertFalse(check_comparison(5.0, 5))
        self.assertFalse(check_comparison(-3, -3))
        
    def test_large_and_small_values(self):
        large = float('inf')
        small = float('-inf')
        # Test with infinity values if supported by the environment's arithmetic logic (Python does support)
        self.assertTrue(large > 0)
        self.assertFalse(small > 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)