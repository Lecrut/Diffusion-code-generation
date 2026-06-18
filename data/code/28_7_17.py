import unittest

def is_greater(value1: float, value2: float) -> bool:
    """Returns True if value1 is strictly larger than value2."""
    return value1 > value2

class TestIsGreater(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_greater(5.0, 3.0))

    def test_negative_numbers(self):
        # Ensure negative numbers are handled correctly (e.g., -1 is greater than -5)
        self.assertTrue(is_greater(-1.0, -5.0))

    def test_zero_and_positive(self):
        self.assertFalse(is_greater(3.0, 4.0))
        self.assertTrue(is_greater(0.0, -1.0))

    def test_equality_edge_case(self):
        # Equality should return False as the function checks for strictly greater
        self.assertFalse(is_greater(7.5, 7.5))

    def test_float_precision(self):
        a = float('inf')
        b = -float('inf')
        self.assertTrue(a > b)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsGreater)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)