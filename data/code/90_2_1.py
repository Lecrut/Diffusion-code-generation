import unittest
class TestOrCondition(unittest.TestCase):
    def test_or_true_true(self):
        self.assertTrue(True or True)
    def test_or_true_false(self):
        self.assertTrue(True or False)
    def test_or_false_true(self):
        self.assertTrue(False or True)
    def test_or_false_false(self):
        self.assertFalse(False or False)
    def test_or_true_empty_string(self):
        self.assertTrue("hello" or "")
    def test_or_empty_string_false(self):
        self.assertFalse("" or False)
    def test_or_none_none(self):
        self.assertIsNone(None or None)
    def test_or_none_true(self):
        self.assertTrue(None or True)
    def test_or_true_none(self):
        self.assertTrue(True or None)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)