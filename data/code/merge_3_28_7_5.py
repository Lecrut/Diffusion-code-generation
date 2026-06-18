import unittest

def is_larger(value):
    """
    Determines if a value is larger than zero.
    
    Args:
        value (int|float): The number to check.
        
    Returns:
        bool: True if the value is greater than 0, False otherwise.
    """
    return value > 0

class TestIsLarger(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(is_larger(1))
        self.assertTrue(is_larger(42))
        self.assertTrue(is_larger(999999))

    def test_negative_integers(self):
        self.assertFalse(is_larger(-1))
        self.assertFalse(is_larger(-50))

    def test_positive_floats(self):
        self.assertTrue(is_larger(0.001))
        self.assertTrue(is_larger(3.14))

    def test_negative_floats(self):
        self.assertFalse(is_larger(-2.718))
        self.assertFalse(is_larger(float("-inf")))

    def test_zero_cases(self):
        # Zero is not larger than zero; it must be strictly greater.
        self.assertFalse(is_larger(0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsLarger)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)