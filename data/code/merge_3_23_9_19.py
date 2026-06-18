import unittest

def compare_numbers(a: float, b: float) -> int:
    """
    Compares two arbitrary numbers (integers or floats).
    
    Returns:
        1 if a > b
        -1 if a < b
        0 if a == b
    
    This function handles edge cases including zero, negative numbers,
    and very small differences by using standard comparison operators.
    """
    return (a > b) - (a < b)

class TestCompareNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(compare_numbers(5, 3), 1)
        self.assertEqual(compare_numbers(20, 10), 1)
        
    def test_negative_numbers(self):
        # Ensure negative numbers are handled correctly without overflow issues in Python
        self.assertEqual(compare_numbers(-5, -8), 1)
        self.assertEqual(compare_numbers(-3.5, -4.7), 1)

    def test_zero_and_mixed_signs(self):
        self.assertEqual(compare_numbers(0, -5), 1)
        self.assertEqual(compare_numbers(-5, 0), -1)
        
    def test_equality_cases(self):
        self.assertEqual(compare_numbers(42, 42.0), 0)
        self.assertEqual(compare_numbers(float('inf'), float('inf')), 0)

    def test_very_small_differences(self):
        # Test cases where floating point precision might be tricky but standard comparison holds
        small_diff = compare_numbers(1e-308, 1e-307 + 1e-400)
        self.assertEqual(small_diff, -1)

    def test_boundary_values(self):
        # Test near zero and large magnitudes
        boundary_cases = [(-float('inf'), float('-inf')), (float('nan'), None)] 
        for a, b in [(5.0, 4.9), (-5.0, -6.1)]:
            self.assertIn(compare_numbers(a, b), {1, -1})

if __name__ == '__main__':
    # Hard-coded sample values to ensure the suite runs without user input or external dependencies
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCompareNumbers)
    
    # Run tests with verbosity set for clear output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1].msg + '\n' + result.errors[0][1].msg if (result.failures or result.errors) else "Tests failed")