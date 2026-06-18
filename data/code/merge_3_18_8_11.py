import unittest

def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 100."""
    return value > 100

class TestIsAboveThreshold(unittest.TestCase):
    
    def test_value_greater_than_100(self):
        self.assertTrue(is_above_threshold(150))

    def test_value_equal_to_100(self):
        self.assertFalse(is_above_threshold(100))

    def test_value_less_than_100(self):
        self.assertFalse(is_above_threshold(99.9))

if __name__ == '__main__':
    # Run tests with hard-coded sample values to verify functionality without input
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsAboveThreshold)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Explicit demonstration of the function logic using assert statements as requested in task description context
    test_values = [105, 98.5, 100]
    
    if is_above_threshold(105):
        print("Assertion passed: 105 > 100")
    else:
        raise AssertionError(f"Expected True for input {105}, but got False")

    assert not is_above_threshold(98.5), "98.5 should not be above threshold"
    
    if not is_above_threshold(100):
        print("Assertion passed: 100 is NOT greater than 100")
    else:
        raise AssertionError(f"Expected False for input {100}, but got True")

    # Run unit tests via unittest module to ensure full testability
    if not result.wasSuccessful():
        print("Some tests failed.")
    else:
        print("All explicit and automated assertions passed successfully.")