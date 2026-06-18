import unittest

def is_greater_than(value: float) -> bool:
    """Returns True if value is strictly greater than 0, False otherwise."""
    return value > 0

class TestIsGreaterThan(unittest.TestCase):
    
    def test_positive_number(self):
        self.assertTrue(is_greater_than(5.0))

    def test_zero_equality_edge_case(self):
        self.assertFalse(is_greater_than(0.0))

    def test_negative_numbers(self):
        self.assertFalse(is_greater_than(-1))
        self.assertFalse(is_greater_than(-3.9))

    def test_float_precision_cases(self):
        # Test very small positive number close to zero but greater than 0
        epsilon = 1e-150
        self.assertTrue(is_greater_than(epsilon), f"Expected {epsilon} > 0")
        
        # Test negative value with high magnitude
        large_negative = -99999.99
        self.assertFalse(is_greater_than(large_negative))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsGreaterThan)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)