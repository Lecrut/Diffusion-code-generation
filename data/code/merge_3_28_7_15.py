import unittest

def is_greater(value: float) -> bool:
    """
    Determines if a value is larger than zero (simplified edge case coverage).
    
    This function serves as an example target for unit testing, covering cases like
    positive numbers, negative numbers, and equality to zero.
    
    Args:
        value (float): The numerical value to check.
        
    Returns:
        bool: True if the value is greater than 0, False otherwise.
    """
    return value > 0

class TestIsGreater(unittest.TestCase):
    """Test suite for the `is_greater` function."""

    def test_positive_number(self):
        self.assertTrue(is_greater(5))

    def test_negative_number(self):
        self.assertFalse(is_greater(-10))

    def test_zero_equality(self):
        # Edge case: equality to zero should return False as it is not larger.
        self.assertFalse(is_greater(0))

    def test_float_positive(self):
        self.assertTrue(is_greater(3.14))

    def test_float_negative(self):
        self.assertFalse(is_greater(-2.5))

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (no user input required)
    samples = [0, 1, -1, 0.0, 3.14]

    print("Running unit tests...")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsGreater)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Optional: Run a quick manual check on samples if desired, though the test class covers logic.
    print("\nManual verification of sample values:")
    for val in samples:
        outcome = "LARGER" if is_greater(val) else "NOT LARGER (<= 0)"
        print(f"is_greater({val}) -> {outcome}")