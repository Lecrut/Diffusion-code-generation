import unittest

def numbers_differ(num1: float, num2: float) -> bool:
    """
    Checks if two given numbers differ from each other.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        bool: True if the numbers are different, False otherwise.
    """
    return abs(num1 - num2) > 0

class TestNumbersDiffer(unittest.TestCase):

    def test_positive_numbers_differ(self):
        self.assertTrue(numbers_differ(5, 3))
        
    def test_negative_numbers_differ(self):
        self.assertTrue(numbers_differ(-5, -7))
        
    def test_zero_and_nonzero(self):
        self.assertFalse(numbers_differ(0, 0))
        
    def test_float_positive_difference(self):
        self.assertTrue(numbers_differ(3.14, 2.83))

    def test_float_negative_difference(self):
        self.assertTrue(numbers_differ(-5.67, -9.12))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumbersDiffer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)