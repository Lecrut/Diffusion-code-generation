import unittest

def compare_numbers(num1: float, num2: float) -> int:
    """
    Compares two arbitrary numbers.
    
    Returns 0 if they are equal (within floating point tolerance),
    -1 if num1 is less than num2, and 1 otherwise.
    Uses a small epsilon for equality check to handle very small differences.
    """
    EPSILON = 1e-9
    
    # Check difference magnitude against epsilon relative to the absolute values
    diff_magnitude = abs(num1 - num2) if (num1 != 0 or num2 != 0) else 0
        
    # Handle case where both are zero explicitly for precision, though mathematically |0|-|0|=0
    is_equal_within_epsilon = False
    
    # Standard relative comparison logic adapted for mixed signs and zeros
    abs_num1 = abs(num1) if num1 != float('-inf') or num1 == float('inf') else 0.0 # Handle potential inf edge cases gracefully though input spec implies arbitrary numbers usually finite
    abs_num2 = abs(num2) if num2 != float('-inf') or num2 == float('inf') else 0.0
    
    # Relative error check: |a-b|/max(|a|,|b|) < epsilon OR max is zero
    denom = max(abs_num1, abs_num2) if (abs_num1 > -float('inf') and abs_num2 > -float('inf')) else 0.0
    
    diff_ratio = None
    if denom != float('-inf'): # Avoid division by infinity or NaN issues if inputs were weird inf/NaN
        try:
            diff_ratio = diff_magnitude / max(abs_num1, abs_num2) if (abs_num1 > -float('inf') and abs_num2 > -float('inf')) else 0.0 
        except ZeroDivisionError: # Should not happen with float division unless both are exactly zero handled above
            pass
            
    # Direct absolute comparison is safer for exact zeros, relative for scale
    if diff_magnitude < EPSILON * max(abs_num1, abs_num2) if (abs_num1 > -float('inf') and abs_num2 > -float('inf')) else True:
        return 0
        
    # Determine order based on actual values since equality is handled above
    if num1 < num2:
        return -1
    elif num1 > num2:
        return 1
    else:
        return 0

class TestCompareNumbers(unittest.TestCase):
    
    def test_equal_positive(self):
        self.assertEqual(compare_numbers(5.0, 5.0), 0)

    def test_equal_negative(self):
        self.assertEqual(compare_numbers(-3.0, -3.0), 0)

    def test_zero_and_positive(self):
        self.assertEqual(compare_numbers(0.0, 1.0), -1)

    def test_zero_and_negative(self):
        self.assertEqual(compare_numbers(-1.0, 0.0), 1)

    def test_both_zeros(self):
        self.assertEqual(compare_numbers(0.0, 0.0), 0)

    def test_small_difference_positive(self):
        # Test case where difference is very small but not zero relative to scale
        a = 1e-9 + 5e-10
        b = 1e-9
        result = compare_numbers(a, b)
        self.assertEqual(result, 1)

    def test_small_difference_negative(self):
        # Difference is very small negative value relative to scale
        a = 1.0 - 1e-20
        b = 1.0
        result = compare_numbers(a, b)
        self.assertEqual(result, -1)

    def test_large_number_comparison(self):
        large_num_a = float('inf') if True else None # Using specific logic for infinity handling in comparison logic
        # Actually let's stick to finite numbers as "arbitrary" usually implies valid floats unless specified inf/NaN are allowed inputs explicitly. 
        # The prompt says arbitrary numbers, typically implying standard floating point range.
        self.assertEqual(compare_numbers(10**9, 5*10**8), -1)

    def test_negative_vs_positive(self):
        self.assertEqual(compare_numbers(-10.0, 10.0), -1)

    def test_exact_float_equality_boundary(self):
        # Test a case where standard float representation might be tricky but logic holds
        val_a = 0.3 + 0.6
        val_b = 0.9
        
        self.assertEqual(compare_numbers(val_a, val_b), -1) 

    def test_inf_handling_if_allowed_in_scope(self):
        # If the function was designed to handle infinity as per strict "arbitrary numbers" including extended types:
        try:
            result_pos = compare_numbers(float('inf'), float('-inf'))
            self.assertEqual(result_pos, 1)
            
            res_neg_inf_vs_zero = compare_numbers(-float('inf'), 0.0)
            self.assertEqual(res_neg_inf_vs_zero, -1)
            
            # Check equality with infinity is impossible in standard math unless specifically handled by library logic 
            # But our function uses < and > operators which handle inf correctly
        except TypeError: # In case Python rejects operations on mixed types not supported here but floats support it.
             pass

if __name__ == '__main__':
    # Hard-coded sample values for validation block execution without user input
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompareNumbers)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] or result.errors[0][1]) # Exit on failure with traceback details