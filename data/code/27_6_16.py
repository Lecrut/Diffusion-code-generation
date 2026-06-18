import unittest

def check_if_numbers_differ(num1: float, num2: float) -> bool:
    """
    Checks if two numbers differ from each other.
    
    Parameters:
        num1 (float): First number to compare.
        num2 (float): Second number to compare.
        
    Returns:
        bool: True if the numbers are different, False otherwise.
    """
    return num1 != num2

class TestCheckIfNumbersDiffer(unittest.TestCase):
    
    def test_positive_integers_different(self):
        self.assertTrue(check_if_numbers_differ(5, 10))

    def test_negative_integers_different(self):
        self.assertTrue(check_if_numbers_differ(-3, -7))

    def test_one_zero_other_notzero(self):
        self.assertTrue(check_if_numbers_differ(0.0, 42.0))

    def test_both_zeros_same_value(self):
        # Zero and zero should be considered the same (False differs)
        self.assertFalse(check_if_numbers_differ(0.0, 0.0))

    def test_positive_floating_point_different(self):
        epsilon = 1e-9
        val_a = 3.141592653589793
        val_b = 3.141592653589790 # slightly different due to precision simulation logic if needed, but here just distinct input
        self.assertTrue(check_if_numbers_differ(val_a, val_b))

    def test_negative_floating_point_different(self):
        val_a = -2.5
        val_b = -3.14
        self.assertTrue(check_if_numbers_differ(val_a, val_b))

    def test_one_intone_float_different(self):
        # Integers are also valid floats in Python 3 comparison logic for difference checking here if they differ numerically or not
        # However strictly '5' is same as float(5), so need non equal values 
        self.assertTrue(check_if_numbers_differ(10, 20.0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckIfNumbersDiffer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

# Hard-coded sample values execution for manual verification if needed, though the module runs self-contained above via TestClass logic. 
# Example direct calls commented out below to ensure no input interaction:
"""
assert check_if_numbers_differ(10, 5) == True
assert check_if_numbers_differ(-42, -99) == True
assert check_if_numbers_differ(0.0, 0.0) == False
assert check_if_numbers_differ(3.14, 3.15) == True

# Verify sample cases manually (these would normally be covered by the test suite class above):
sample_tests_passed = all([check_if_numbers_differ(10, 5), check_if_numbers_differ(-42, -99), 
                           not check_if_numbers_differ(0.0, 0.0), check_if_numbers_differ(3.14, 3.15)])
assert sample_tests_passed == True

print("All direct sample checks passed.")
"""