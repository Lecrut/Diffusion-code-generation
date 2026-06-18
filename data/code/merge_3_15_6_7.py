import unittest

def check_equality(a: any, b: any) -> bool:
    """
    Checks if two values are equal using standard equality operators.
    
    This function handles integers, floats, strings, and other comparable types.
    For floating-point numbers, it uses the default float identity operator (==),
    which may behave unexpectedly for very close but not identical binary representations.
    To handle potential precision issues in some test scenarios explicitly requiring 
    approximate equality, a dedicated 'approx_equal' function could be added later.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        bool: True if a equals b, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(check_equality(5, 5))
        self.assertFalse(check_equality(5, 6))
        self.assertTrue(check_equality(-10, -10))

if __name__ == '__main__':
    pass
