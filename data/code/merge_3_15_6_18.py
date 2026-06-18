import unittest

def check_equality(a: any, b: any) -> bool:
    """
    Checks if two values are equal using Python's built-in equality operator.
    
    This function is designed to be testable and handles various input types 
    including integers, floats, strings, lists, dictionaries, etc., by relying 
    on the standard identity of objects in Python (the '==' operator).

    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if a is equal to b, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):
    
    def test_integers(self):
        self.assertEqual(check_equality(5, 5), True)
        self.assertEqual(check_equality(10, 20), False)
        
    def test_floats(self):
        # Floating point comparison can be tricky due to precision issues. 
        # We compare exact representations here as per standard equality rules.
        self.assertEqual(check_equality(3.14, 3.14), True)
        self.assertNotEqual(check_equality(3.14, 3.15), False) 
        
    def test_strings(self):
        self.assertEqual(check_equality("hello", "hello"), True)
        self.assertEqual(check_equality("", ""), True)
        self.assertNotEqual(check_equality("test", "testing"), False)

if __name__ == '__main__':
    # Hard-coded sample values to run tests without user input or files.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckEquality)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        print("Some tests failed.")
        exit(1)