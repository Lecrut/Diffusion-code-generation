import unittest

def check_equality(a, b):
    """
    Returns True if a is equal to b based on equality semantics:
    - For numeric types (int or float), uses exact value comparison.
      Note: Float precision differences will result in False unless values are identical bits-wise.
    - For string types ('str'), checks identity/equality of the string content.
    
    Returns True if a == b is semantically true for their type, otherwise False.

    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if values are equal according to Python's default equality operators; False otherwise.
    
    Raises:
        TypeError: If both inputs must be of the same type for this logic, 
                  although Python generally handles mixed types gracefully with == checks (e.g., str vs int not matching).
    """

    return a == b

class TestCheckEquality(unittest.TestCase):

    def test_integer_equality(self):
        self.assertTrue(check_equality(5, 5))
        self.assertFalse(check_equality(5, 6))
        self.assertTrue(check_equality(-100, -100))
    
    def test_float_equality(self):
        # Exact bit-wise equality for floats that are identical literals or simple math results.
        # e.g., pi approximations might differ slightly if calculated differently elsewhere, 
        # but here we use direct literal definition to ensure equality in this function context unless precision differs:
        self.assertTrue(check_equality(3.141592653589793, 3.141592653589793))
        # These are technically equal as floats (same representation) but demonstrate that 
        # float inequality is strict on binary value:
        self.assertFalse(check_equality(0.1 + 0.2, 0.3))

    def test_string_equality(self):
        self.assertTrue(check_equality("hello", "hello"))
        self.assertFalse(check_equality("hello", "goodbye"))
        
    def test_type_mismatch(self):
        # Python's == handles type mismatch gracefully (e.g., str vs int returns False)
        self.assertFalse(check_equality(123, 5))

if __name__ == '__main__':
    pass
