import unittest

def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 100."""
    return value > 100

class TestIsAboveThreshold(unittest.TestCase):
    
    def test_value_greater_than_threshold(self):
        self.assertTrue(is_above_threshold(150))

    def test_value_equal_to_threshold(self):
        self.assertFalse(is_above_threshold(100))

    def test_value_less_than_threshold(self):
        self.assertFalse(is_above_threshold(90))

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    samples = [25, 100, 101]
    
    print("Running manual checks on sample values:")
    for val in samples:
        result = is_above_threshold(val)
        status = "Above" if result else "Not above"
        print(f"{val}: {status}")

    # Run the unit tests to ensure they pass
    unittest.main(verbosity=2, exit=False)