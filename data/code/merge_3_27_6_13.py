import unittest

def check_difference(num1: float, num2: float) -> bool:
    """Check if two numbers differ (are not equal)."""
    return abs(num1 - num2) > 0

class TestDifference(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertTrue(check_difference(5.0, 10.0))

    def test_negative_numbers(self):
        self.assertFalse(check_difference(-3.0, -7.0))

    def test_mixed_signs(self):
        self.assertEqual(check_difference(-2.0, 4.0), True)

    def test_zero_values(self):
        # First zero should fail (they are equal), second pass (one is non-zero)
        self.assertFalse(check_difference(0.0, -5.1))
        
    def test_float_precision(self):
        a = float('inf') + 2
        b = float('inf')
        self.assertTrue(check_difference(a, b))

if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDifference)