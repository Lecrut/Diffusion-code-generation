import unittest

def check_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")
    return not a and not b

class TestCheckBothFalse(unittest.TestCase):
    def test_both_false_true(self):
        self.assertTrue(check_both_false(False, False))
    
    def test_one_false(self):
        with self.assertRaises(ValueError):
            check_both_false(True, False)
        with self.assertRaises(ValueError):
            check_both_false(False, True)
    
    def test_both_true(self):
        with self.assertRaises(ValueError):
            check_both_false(True, True)
    
    def test_invalid_input_types(self):
        with self.assertRaises(ValueError):
            check_both_false(1, 2)
        with self.assertRaises(ValueError):
            check_both_false('a', 'b')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)