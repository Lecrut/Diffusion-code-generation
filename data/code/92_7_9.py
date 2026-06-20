import unittest

def opposite_truth(value):
    return not value

class TestOppositeTruth(unittest.TestCase):
    def test_true(self):
        self.assertFalse(opposite_truth(True))

    def test_false(self):
        self.assertTrue(opposite_truth(False))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOppositeTruth('test_true'))
    suite.addTest(TestOppositeTruth('test_false'))
    runner = unittest.TextTestRunner()
    runner.run(suite)