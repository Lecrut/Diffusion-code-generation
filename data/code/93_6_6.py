import unittest

def both_false(a, b):
    return not a and not b

class TestBothFalse(unittest.TestCase):
    def test_both_false(self):
        self.assertTrue(both_false(False, False))
        self.assertFalse(both_false(True, False))
        self.assertFalse(both_false(False, True))
        self.assertFalse(both_false(True, True))

if __name__ == '__main__':
    unittest.main()