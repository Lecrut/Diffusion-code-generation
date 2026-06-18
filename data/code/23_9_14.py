import unittest

def compare_numbers(a: float, b: float) -> int:
    """
    Compares two arbitrary numbers and returns a result indicating their relationship.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        int: -1 if a < b, 0 if a == b, 1 if a > b
        
    Handles edge cases including zero, negative numbers, and very small differences
    by using standard floating-point comparison logic suitable for Python's default behavior.
    """
    return (a > b) - (a < b)

class TestCompareNumbers(unittest.TestCase):
    
    def test_positive_integers_equal(self):
        self.assertEqual(compare_numbers(5, 5), 0)

    def test_negative_integers_equal(self):
        self.assertEqual(compare_numbers(-10, -10), 0)

    def test_zero_and_negatives_equal(self):
        self.assertEqual(compare_numbers(0.0, -0.0), 0)
        
    def test_positive_vs_greater_negative(self):
        self.assertEqual(compare_numbers(5, -3), 1)

    def test_less_vs_greater_negative(self):
        self.assertEqual(compare_numbers(-7, -2), -1)

    def test_zero_difference_floats(self):
        # Testing very small differences that might theoretically be zero due to precision limits in float math if constructed this way, 
        # though standard floats usually distinguish them unless they are the same value.
        val = 0.0 + (3.7e-8) - 1 / 2**34
        self.assertEqual(compare_numbers(val, 0), 0)

    def test_very_small_difference_not_zero(self):
        # A very small difference that should result in a non-zero return value if the numbers are distinct 
        # and not identical within floating point precision limits.
        diff = compare_numbers(1e-25 + 1, 1e-25)
        self.assertNotEqual(diff, 0)

    def test_large_values(self):
        large_a = float('inf') - 1
        large_b = float('-inf') + 1
        # inf minus something is still effectively larger than neg_inf plus something
        result = compare_numbers(large_a, large_b)
        self.assertEqual(result, 1)

    def test_exact_zero_case(self):
        a, b = 0.0, 0.0
        expected_result = compare_numbers(a, b)
        self.assertEqual(expected_result, 0)

if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompareNumbers)
    
    # Run the test suite with results printed directly to stdout/err
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)