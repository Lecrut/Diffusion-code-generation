import unittest

class TestOrCondition(unittest.TestCase):
    def test_or_true_true(self):
        self.assertTrue(self.eval_or(True, True))

    def test_or_true_false(self):
        self.assertTrue(self.eval_or(True, False))
        self.assertTrue(self.eval_or(False, True))

    def test_or_false_true(self):
        self.assertTrue(self.eval_or(False, True))
        self.assertTrue(self.eval_or(True, False))

    def test_or_false_false(self):
        self.assertFalse(self.eval_or(False, False))

    def eval_or(self, a, b):
        return a or b

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)