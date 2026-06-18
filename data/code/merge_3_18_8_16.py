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
        self.assertFalse(is_above_threshold(90))

if __name__ == '__main__':
    # Run tests with hard-coded sample values directly for demonstration if needed, 
    # but the primary execution via unittest is shown below.
    
    print("Running manual checks...")
    assert 150 > 100 and is_above_threshold(150), "Test failed: value greater than threshold"
    assert not (90 > 100) and not is_above_threshold(90), "Test failed: value less than threshold"
    print("All manual assertions passed.")

    # Optional: Run the unit test suite if desired by uncommenting below, 
    # though typically 'python script.py' runs unittest automatically.
    # unittest.main()