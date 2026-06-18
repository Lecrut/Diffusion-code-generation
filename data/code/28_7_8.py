import unittest

def is_greater(value):
    """
    Determines if a value is larger than 0.
    
    Parameters:
        value (int | float): The number to check.
        
    Returns:
        bool: True if value > 0, False otherwise.
    """
    return value > 0

class TestIsGreater(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(is_greater(5))

    def test_negative_integer(self):
        self.assertFalse(is_greater(-10))

    def test_zero(self):
        # Edge case: equality to zero should return False as it is not larger.
        self.assertFalse(is_greater(0))

    def test_positive_float(self):
        self.assertTrue(is_greater(3.14))

    def test_negative_float(self):
        self.assertFalse(is_greater(-2.5))

if __name__ == '__main__':
    # Run tests with hard-coded sample values implicitly covered by the TestCase methods
    unittest.main()