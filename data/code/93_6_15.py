import unittest

FALSE = False
TRUE = True

def check_both_false(a, b):
    return not a and not b

class TestCheckBothFalse(unittest.TestCase):
    def test_both_false_true(self):
        self.assertTrue(check_both_false(FALSE, FALSE))

    def test_one_false(self):
        self.assertFalse(check_both_false(TRUE, FALSE))
        self.assertFalse(check_both_false(FALSE, TRUE))

    def test_both_true(self):
        self.assertFalse(check_both_false(TRUE, TRUE))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)