import unittest

def check_both_false(a, b):
    if not a and not b:
        return True
    return False

class TestCheckBothFalse(unittest.TestCase):
    def test_both_false_true(self):
        self.assertTrue(check_both_false(False, False))
    
    def test_one_false(self):
        self.assertFalse(check_both_false(True, False))
        self.assertFalse(check_both_false(False, True))
    
    def test_both_true(self):
        self.assertFalse(check_both_false(True, True))
    
    def test_both_true_with_different_values(self):
        self.assertFalse(check_both_false(1, 1))
        self.assertFalse(check_both_false(0, 0))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)