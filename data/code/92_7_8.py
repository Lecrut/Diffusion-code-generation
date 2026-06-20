import unittest

def opposite_truth(value):
    return not value

class TestOppositeTruth(unittest.TestCase):

    def test_true(self):
        self.assertFalse(opposite_truth(True))

    def test_false(self):
        self.assertTrue(opposite_truth(False))
if __name__ == '__main__':
    print(opposite_truth(True))
    print(opposite_truth(False))
    unittest.main()