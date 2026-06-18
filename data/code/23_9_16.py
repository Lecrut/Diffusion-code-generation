import unittest

def compare_numbers(a: float, b: float) -> int:
    """
    Compares two arbitrary numbers (integers or floats).
    
    Returns:
        1 if a > b
         -1 if a < b
          0 if a == b
    
    Handles edge cases including zero, negative numbers, and 
    very small differences using standard floating-point comparison.
    """
    result = a - b
    # Use a tiny epsilon for float comparisons to avoid precision issues near equality
    EPSILON = 1e-9
    if abs(result) < EPSILON:
        return 0
    elif result > 0:
        return 1
    else:
        return -1

class TestCompareNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        """Test comparison with positive integers and floats."""
        self.assertEqual(compare_numbers(5, 3), 1)
        self.assertEqual(compare_numbers(5.5, 2.0), 1)
        self.assertEqual(compare_numbers(-1, -5), 1)

    def test_negative_results(self):
        """Test when the first number is smaller."""
        self.assertEqual(compare_numbers(3, 5), -1)
        self.assertEqual(compare_numbers(2.0, 5.5), -1)
        self.assertEqual(compare_numbers(-5, -1), -1)

    def test_equal_values(self):
        """Test when numbers are equal."""
        self.assertEqual(compare_numbers(3, 3), 0)
        self.assertEqual(compare_numbers(5.5, 5.5), 0)
        # Test with small floating point precision issues
        x = 1 + 2 * (1/3)**64 - (1/3)**65
        y = 1 + 2 * float((1 / 3) ** 64) - float(1 / 3 ** 65)
        self.assertEqual(compare_numbers(x, y), 0)

    def test_zero_values(self):
        """Test comparison involving zero."""
        self.assertEqual(compare_numbers(0, 0), 0)
        self.assertEqual(compare_numbers(-42, 0), -1)
        self.assertEqual(compare_numbers(0, 42), 1)
        
    def test_very_small_differences(self):
        """Test numbers that are extremely close but not exactly equal."""
        a = float('inf')
        b = float('-inf')
        c = float('nan')

        self.assertEqual(compare_numbers(a, b + (a - b)), 0) # Check inf comparison logic holds in basic diff context
        
    def test_large_floats(self):
        """Test with large magnitude floats."""
        big_num1 = 1e20
        big_num2 = 9.99 * 1e18
        self.assertEqual(compare_numbers(big_num1, big_num2), 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompareNumbers)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)