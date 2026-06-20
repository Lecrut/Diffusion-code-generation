import unittest

class TestOrCondition(unittest.TestCase):
    def test_true_or_true(self):
        self.assertTrue(True or True)

    def test_true_or_false(self):
        self.assertTrue(True or False)

    def test_false_or_true(self):
        self.assertTrue(False or True)

    def test_false_or_false(self):
        self.assertFalse(False or False)

    def test_false_or_zero(self):
        self.assertEqual(0 or 5, 5)

    def test_empty_string_or_true(self):
        self.assertTrue("" or True)

    def test_none_or_true(self):
        self.assertTrue(None or True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)