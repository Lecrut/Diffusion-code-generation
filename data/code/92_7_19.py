import unittest

def opposite_truth(value):
    return not value

class TestOppositeTruth(unittest.TestCase):

    def test_true(self):
        self.assertFalse(opposite_truth(True))

    def test_false(self):
        self.assertTrue(opposite_truth(False))
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOppositeTruth)
    unittest.TextTestRunner(verbosity=2).run(suite)
print(opposite_truth(True))
print(opposite_truth(False))