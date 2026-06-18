import unittest

def is_larger(value):
    """
    Determines if a value is larger than zero.
    
    Args:
        value (int, float): The number to check.
        
    Returns:
        bool: True if the value is strictly greater than 0, False otherwise.
    """
    return value > 0

class TestIsLarger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(is_larger(1))
        self.assertTrue(is_larger(42))
        
    def test_negative_integer(self):
        self.assertFalse(is_larger(-5))
        self.assertFalse(is_larger(-0.001))
        
    def test_zero_edge_case(self):
        """Test that zero is not considered larger."""
        self.assertFalse(is_larger(0))
        
    def test_float_positive(self):
        self.assertTrue(is_larger(3.14))
        self.assertTrue(is_larger(1e-5))
        
    def test_float_negative(self):
        self.assertFalse(is_larger(-2.718))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate the function behavior directly before running tests
    samples = [
        (10, True),
        (-5, False),
        (0, False),
        (3.14, True),
        (-0.001, False)
    ]
    
    print("Testing is_larger function with sample values:")
    for val, expected in samples:
        result = is_larger(val)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_larger({val}) -> {result} (Expected: {expected}) [{status}]")

    # Run the unit tests suite
    unittest.main(verbosity=2, exit=False)