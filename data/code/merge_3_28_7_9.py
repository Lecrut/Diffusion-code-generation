import unittest

def is_larger(value):
    """
    Determines if a value is larger than 0.
    
    Args:
        value (int/float): The number to check.
        
    Returns:
        bool: True if the value is strictly greater than 0, False otherwise.
    """
    return value > 0

class TestIsLarger(unittest.TestCase):
    def test_positive_number(self):
        self.assertTrue(is_larger(5))

    def test_negative_number(self):
        self.assertFalse(is_larger(-10))

    def test_zero_edge_case(self):
        # Zero is not larger than zero, so it should return False.
        self.assertFalse(is_larger(0))

    def test_float_positive(self):
        self.assertTrue(is_larger(3.5))

    def test_float_negative(self):
        self.assertFalse(is_larger(-2.7))

if __name__ == '__main__':
    # Run the tests with hard-coded sample values logic implicitly handled by TestCase methods.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsLarger)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)