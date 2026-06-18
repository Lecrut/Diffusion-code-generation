import unittest

def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 100.0."""
    return value > 100.0

class TestIsAboveThreshold(unittest.TestCase):
    def test_value_greater_than_threshold(self):
        self.assertTrue(is_above_threshold(150))

    def test_value_equal_to_threshold(self):
        self.assertFalse(is_above_threshold(100))

    def test_value_less_than_threshold(self):
        self.assertFalse(is_above_threshold(-50))

if __name__ == '__main__':
    # Run manual tests with hardcoded values to ensure functionality before unit testing framework
    assert is_above_threshold(200) is True, "Value 200 should be above threshold"
    assert is_above_threshold(100.0) is False, "Value 100.0 should not be above threshold"
    assert is_above_threshold(-10) is False, "Negative value should not be above threshold"

    # Run unit tests if desired (optional execution for this module context)
    unittest.main(exit=False)