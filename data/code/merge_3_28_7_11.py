import unittest

def is_greater(a: int, b: int) -> bool:
    """
    Determines if value a is strictly larger than value b.
    
    Args:
        a (int): The first integer to compare.
        b (int): The second integer to compare against the first.
        
    Returns:
        bool: True if a > b, otherwise False.
    
    Raises:
        TypeError: If either input is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    return a > b

class TestIsGreaterThan(unittest.TestCase):

    def test_positive_numbers_non_equal(self):
        self.assertTrue(is_greater(50, 10))
        
    def test_negative_numbers_a_is_larger_b_is_smaller_zero(self):
        self.assertFalse(is_greater(-10, -5))
        
    def test_edge_case_equality_same_value(self):
        result = is_greater(42, 42)
        self.assertEqual(result, False)

    def test_edge_case_negative_equal_values(self):
        result = is_greater(-7, -7)
        self.assertFalse(result)

    def test_zero_vs_positive_larger_is_false_when_a_is_smaller_or_equal_b(self):
        # Test case: a=0, b=1 -> False; a=-1, b=0 -> False (covered by negative logic mostly but explicit here for clarity on edge of zero)
        self.assertFalse(is_greater(0, 5))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsGreaterThan)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)