import unittest

def or_condition(a, b):
    return a or b

class TestOrCondition(unittest.TestCase):
    def test_true_or_true(self):
        self.assertTrue(or_condition(True, True))

    def test_true_or_false(self):
        self.assertTrue(or_condition(True, False))

    def test_false_or_true(self):
        self.assertTrue(or_condition(False, True))

    def test_false_or_false(self):
        self.assertFalse(or_condition(False, False))

if __name__ == '__main__':
    unittest.main()