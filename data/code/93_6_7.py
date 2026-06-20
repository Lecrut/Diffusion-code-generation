import unittest

def both_false(a, b):
    return not a and not b

class TestBothFalse(unittest.TestCase):
    def test_both_false_true(self):
        self.assertTrue(both_false(False, False))

    def test_both_false_false(self):
        self.assertFalse(both_false(True, False))
        self.assertFalse(both_false(False, True))
        self.assertFalse(both_false(True, True))

if __name__ == '__main__':
    unittest.main()