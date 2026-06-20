import unittest

class OrConditionTest(unittest.TestCase):
    def test_true_or_true(self):
        self.assertTrue(True or True)

    def test_true_or_false(self):
        self.assertTrue(True or False)
        self.assertTrue(False or True)

    def test_false_or_true(self):
        self.assertTrue(False or True)
        self.assertTrue(True or False)

    def test_false_or_false(self):
        self.assertFalse(False or False)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)