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
    def test_opposite_with_other_values(self):
        self.assertTrue(find_opposite(1))
        self.assertFalse(find_opposite(0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)