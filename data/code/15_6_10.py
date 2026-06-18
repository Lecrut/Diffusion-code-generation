import unittest

def check_equality(a, b):
    """
    Checks if two values a and b are equal using Python's built-in equality operator.
    
    Args:
        a (any): First value to compare.
        b (any): Second value to compare.
        
    Returns:
        bool: True if a == b, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):
    def test_integers_equal(self):
        self.assertTrue(check_equality(5, 5))

    def test_integers_not_equal(self):
        self.assertFalse(check_equality(5, 10))

    def test_floats_equal(self):
        # Note: Floating point equality can be tricky due to precision. 
        # This tests exact representation as per standard == behavior unless specified otherwise.
        self.assertTrue(check_equality(3.14, 3.14))
        
    def test_floats_not_equal(self):
        self.assertFalse(check_equality(3.14, 3.15))

    def test_strings_equal(self):
        self.assertTrue(check_equality("hello", "hello"))

    def test_strings_not_equal(self):
        self.assertFalse(check_equality("hello", "world"))

if __name__ == '__main__':
    # Run the tests with hardcoded sample values implicitly covered by unit methods.
    unittest.main()