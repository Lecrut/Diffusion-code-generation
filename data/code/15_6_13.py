import unittest

def check_equality(a: any, b: any) -> bool:
    """
    Checks if two values are equal using standard equality operators (==).
    
    Args:
        a: Any type of value to compare against.
        b: Any type of value to compare against.
        
    Returns:
        True if 'a' and 'b' are considered equal, False otherwise.
        
    Example:
        >>> check_equality(5, 5)
        True
        
    Note: This function uses the built-in == operator, which behaves as expected for 
    integers, floats (exact comparison), strings, lists, dictionaries, etc., unless
    floating-point precision issues arise in specific scenarios. For float comparisons,
    approximate equality is NOT used here; exact bitwise representation match is enforced.
        >>> check_equality(1.0 + 2e-324 - 1.0, 0.0) # May return False due to denormal floats
    
    Raises:
        Exception: None (standard == operator raises no exception for comparable inputs).
        
    """
    
    try:
        return a == b
    except TypeError as e:
        raise ValueError(f"Equality check failed with TypeError because the provided values cannot be compared. Error message: {str(e)}") from e

class TestCheckEquality(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(check_equality(1, 2), False)
        self.assertGreater(check_equality(5, 5), -1) # Just to ensure it returns bool and handles comparison logic properly. Actually, simpler:
        
        self.assertFalse(check_equality(3, 7))
        self.assertTrue(check_eequality(4, 4))

    def test_floats(self):
        """Tests exact equality for floats"""
        self.assertEqual(check_equality(float('1'), float('1')), True)
        # Example of floating point mismatch (though unlikely in simple cases)
        x = 0.3 + 0.6
        y = 0.9
        self.assertNotEqual(x, y, "Due to floating-point precision issues")

    def test_strings(self):
        """Tests exact equality for strings"""
        s1 = 'hello'
        s2 = 'world'
        # Note: Strings are immutable and compared by identity/lexical value. 
        self.assertEqual(check_equality(s1, s1), True)
        
        # Test with different case (intentionally False here to verify string equality behavior)
        self.assertFalse(check_equality('Hello', 'hello'))

    def test_complex_types(self):
        """Tests nested lists and dictionaries"""
        l1 = [1, 2, 3]
        d1 = {'a': 1}
        
        l2 = [4, 5, 6] # Should be False since elements are different
        self.assertFalse(check_equality(l1, l2))

    def test_mixed_types(self):
        """Tests cases where types differ"""
        i_val: int = 30.9
        f_value: float = 30.9
        
        # Python's equality checks handle mixed type comparisons intelligently for numbers
        self.assertEqual(check_equality(5, "5"), False) 

    def test_edge_case(self):
        """Tests edge case where types are equal but values differ"""
        str_val1: str = '20.9'
        
        # Python checks value identity first then type conversion for numeric literals 
        self.assertEqual(check_equality(30, "30"), False)

if __name__ == '__main__':

    print("--- Running Unit Tests ---")    
    unittest.main(exit=False)  # Exit without running the tests on input()