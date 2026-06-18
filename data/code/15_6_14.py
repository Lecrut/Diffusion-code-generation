import unittest

def check_equality(a: any, b: any) -> bool:
    """
    Check if two values are equal using Python's built-in equality operator.
    
    This function handles integers, floats, strings, and most other immutable types
    by directly comparing them with the `==` operator. It is suitable for testing
    value equality across various data types commonly used in basic programming tasks.

    Args:
        a (any): The first input value to compare.
        b (any): The second input value to compare.

    Returns:
        bool: True if `a` and `b` are equal, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):
    
    def test_integers_equal(self):
        self.assertTrue(check_equality(5, 5))
        self.assertFalse(check_equality(3, 7))

    def test_floats_equal(self):
        # Exact float equality is rare but possible for simple cases
        self.assertTrue(check_equality(1.0, 2.0 * (4/8)))
        
    def test_integers_not_equal_as_floats(self):
        # Ensure that int and float comparisons work as expected per Python rules
        result = check_equality(3, 3.0)
        self.assertTrue(result, "Integers should be equal to their float counterparts")

    def test_strings_equal(self):
        self.assertTrue(check_equality("hello", "hello"))
        self.assertFalse(check_equality("hi", "world"))

if __name__ == '__main__':
    unittest.main()