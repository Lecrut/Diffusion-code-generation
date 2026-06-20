import unittest

def both_false(a, b):
    return not a and not b

class TestBothFalse(unittest.TestCase):
    def test_both_true(self):
        self.assertFalse(both_false(True, True))

    def test_first_true_second_false(self):
        self.assertFalse(both_false(True, False))

    def test_first_false_second_true(self):
        self.assertFalse(both_false(False, True))

    def test_both_false(self):
        self.assertTrue(both_false(False, False))

if __name__ == '__main__':
    unittest.main()