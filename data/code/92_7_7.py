import unittest

def opposite_truth(value):
    return not value

class TestOppositeTruth(unittest.TestCase):

    def test_true(self):
        self.assertFalse(opposite_truth(True))

    def test_false(self):
        self.assertTrue(opposite_truth(False))

    def test_none(self):
        self.assertIsNone(opposite_truth(None))

    def test_int_zero(self):
        self.assertTrue(opposite_truth(0))

    def test_int_nonzero(self):
        self.assertFalse(opposite_truth(1))

if __name__ == '__main__':
    unittest.main()