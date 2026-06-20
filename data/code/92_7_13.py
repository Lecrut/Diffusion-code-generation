import unittest

def opposite_truth(value):
    return not value

class TestOppositeTruth(unittest.TestCase):
    def test_boolean_values(self):
        self.assertFalse(opposite_truth(True))
        self.assertTrue(opposite_truth(False))

    def test_integer_values(self):
        self.assertFalse(opposite_truth(1))
        self.assertTrue(opposite_truth(0))

    def test_string_values(self):
        self.assertFalse(opposite_truth("hello"))
        self.assertTrue(opposite_truth(""))

    def test_none_value(self):
        self.assertTrue(opposite_truth(None))

if __name__ == '__main__':
    unittest.main()