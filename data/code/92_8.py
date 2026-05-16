import unittest
def find_opposite(boolean_input):
    return not boolean_input
class TestOppositeTruthValue(unittest.TestCase):
    def test_opposite_true(self):
        self.assertTrue(find_opposite(True))
    def test_opposite_false(self):
        self.assertFalse(find_opposite(False))
    def test_opposite_true_multiple(self):
        self.assertTrue(find_opposite(True))
    def test_opposite_false_multiple(self):
        self.assertFalse(find_opposite(False))
    def test_opposite_mixed_inputs(self):
        test_cases = [True, False]
        for value in test_cases:
            expected = not value
            actual = find_opposite(value)
            self.assertEqual(actual, expected, f"Failed for input: {value}")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)