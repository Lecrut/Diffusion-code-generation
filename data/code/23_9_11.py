import unittest

def compare_numbers(num1: float, num2: float) -> int:
    """
    Compares two arbitrary numbers (integers or floats).
    
    Returns:
        0 if num1 == num2 within floating-point tolerance for very small differences.
        -1 if num1 < num2.
        1 if num1 > num2.
        
    This function handles edge cases such as zero, negative numbers, and 
    values with very small differences by using a relative/absolute hybrid epsilon check.
    """
    # Define tolerance for floating-point comparisons to handle "very small differences"
    EPSILON = 1e-9
    
    if abs(num1 - num2) < EPSILON:
        return 0
    elif num1 > num2:
        return 1
    else:
        return -1

class TestCompareNumbers(unittest.TestCase):
    
    def test_positive_integers(self):
        """Test comparison of positive integers."""
        self.assertEqual(compare_numbers(5, 3), 1)
        self.assertEqual(compare_numbers(2, 7), -1)
        self.assertEqual(compare_numbers(4, 4), 0)

    def test_negative_integers(self):
        """Test comparison of negative integers."""
        self.assertEqual(compare_numbers(-2, -5), 1)
        self.assertEqual(compare_numbers(-8, -3), -1)
        self.assertEqual(compare_numbers(-4, -4), 0)

    def test_zero_and_mixed_signs(self):
        """Test cases involving zero and mixed positive/negative numbers."""
        self.assertEqual(compare_numbers(0, 5), -1)
        self.assertEqual(compare_numbers(-3, 0), -1)
        self.assertEqual(compare_numbers(0, -2), 1)
        self.assertEqual(compare_numbers(0, 0), 0)

    def test_floats_with_small_difference(self):
        """Test floating-point numbers with very small differences."""
        # Differences smaller than EPSILON should be considered equal
        self.assertEqual(compare_numbers(1.0 + 1e-9, 1.0), 0)
        self.assertEqual(compare_numbers(-5.0 - 1e-10, -5.0), 0)
        
        # Differences larger than EPSILON must distinguish correctly
        diff = compare_numbers(1.0 + 2 * 1e-9, 1.0)
        self.assertNotEqual(diff, 0)
        self.assertEqual(diff, 1)

    def test_large_magnitude_floats(self):
        """Test floating-point numbers with large magnitudes."""
        # Large positive vs negative
        self.assertEqual(compare_numbers(1e20, -1e20), 1)
        
        # Two large positives where one is slightly larger but not within epsilon of the other
        val_a = 3.5 * 1e9 + 100
        val_b = 3.5 * 1e9
        self.assertEqual(compare_numbers(val_a, val_b), 1)

    def test_edge_case_exact_floats(self):
        """Test cases where floats are mathematically equal."""
        # These should be exactly zero difference if represented identically in binary float
        self.assertEqual(compare_numbers(0.5 + (2**-32), 0.5 + (2**-32)), 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompareNumbers)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)