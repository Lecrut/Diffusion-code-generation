import unittest

def check_both_false(a, b):
    return not a and not b

class TestCheckBothFalse(unittest.TestCase):
    def test_both_false_true(self):
        self.assertTrue(check_both_false(False, False))
    
    def test_one_false(self):
        self.assertFalse(check_both_false(True, False))
        self.assertFalse(check_both_false(False, True))
    
    def test_both_true(self):
        self.assertFalse(check_both_false(True, True))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)