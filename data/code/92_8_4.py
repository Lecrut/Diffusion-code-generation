import unittest
def find_opposite(value):
    return not value
class TestOppositeTruthValue(unittest.TestCase):
    def test_opposite_true(self):
        self.assertTrue(find_opposite(True))
    def test_opposite_false(self):
        self.assertFalse(find_opposite(False))
    def test_opposite_true_input(self):
        self.assertTrue(find_opposite(True))
    def test_opposite_false_input(self):
        self.assertFalse(find_opposite(False))
    def test_opposite_zero_as_boolean(self):
        self.assertFalse(find_opposite(0))
    def test_opposite_one_as_boolean(self):
        self.assertTrue(find_opposite(1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)