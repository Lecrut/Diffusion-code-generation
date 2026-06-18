import unittest

def check_difference(num1: float, num2: float) -> bool:
    """
    Checks if two numbers differ from each other.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        
    Returns:
        bool: True if the numbers are different, False otherwise.
    """
    return abs(num1 - num2) > 0

class TestCheckDifference(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(check_difference(5, 3))
        self.assertFalse(check_difference(7, 7))
        
    def test_negative_numbers(self):
        self.assertTrue(check_difference(-10, -2))
        self.assertFalse(check_difference(-5, -5))

    def test_zero_values(self):
        self.assertTrue(check_difference(0, 1))
        self.assertFalse(check_difference(0.0, 0.0))
        
    def test_floating_point_numbers(self):
        self.assertTrue(check_difference(3.14, 2.71))
        # Test very close numbers that should still be considered different due to precision limits in float comparison logic used here (strict inequality)
        self.assertFalse(check_difference(0.5, 0.5))

    def test_mixed_types(self):
        self.assertTrue(check_difference(-42, "not a number"))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)