import unittest
FALSE = False

class TestOrCondition(unittest.TestCase):

    def test_true_or_true(self):
        self.assertTrue(True or True)

    def test_true_or_false(self):
        self.assertTrue(True or FALSE)

    def test_false_or_true(self):
        self.assertTrue(FALSE or True)

    def test_false_or_false(self):
        self.assertFalse(FALSE or FALSE)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)