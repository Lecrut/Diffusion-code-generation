import unittest

def numbers_differ(a: float, b: float) -> bool:
    """
    Checks if two numbers differ from each other.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        bool: True if the numbers are not equal, False otherwise.
    """
    return a != b

class TestNumbersDiffer(unittest.TestCase):
    """Test suite for the numbers_differ function."""

    def test_positive_integers(self):
        self.assertTrue(numbers_differ(10, 20))
        self.assertFalse(numbers_differ(5, 5))

    def test_negative_integers(self):
        self.assertTrue(numbers_differ(-3, -7))
        self.assertFalse(numbers_differ(0, 0))

    def test_zero_cases(self):
        # Zero differing from a non-zero number
        self.assertTrue(numbers_differ(0, 5))
        self.assertTrue(numbers_differ(-100, 0))
        # Two zeros should not differ
        self.assertFalse(numbers_differ(0, 0))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(3.14, 2.71))
        self.assertTrue(numbers_differ(-0.5, 0.5))
        # Floating point equality edge case (same value)
        self.assertFalse(numbers_differ(3.14159, 3.14159))

    def test_mixed_types(self):
        """Ensure integers and floats are handled correctly."""
        self.assertTrue(numbers_differ(10, 20.0))
        self.assertFalse(numbers_differ(5, float(5)))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumbersDiffer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else None)