import unittest

def is_larger_than(value: float, threshold: float) -> bool:
    """Returns True if value > threshold."""
    return value > threshold

class TestIsLarger(unittest.TestCase):
    
    def test_equal_values(self):
        result = is_larger_than(5.0, 5.0)
        self.assertFalse(result)

    def test_negative_numbers_smaller_threshold(self):
        result = is_larger_than(-2.3, -10.0)
        self.assertTrue(result)

    def test_negative_number_equal_to_positive_threshold(self):
        # Should be False (negative < positive)
        result = is_larger_than(-5.0, 3.7)
        self.assertFalse(result)

    def test_large_magnitude_values(self):
        result = is_larger_than(1e10, 2e9)
        self.assertTrue(result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsLarger)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)