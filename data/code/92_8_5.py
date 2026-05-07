import unittest
class TestOppositeTruthValue(unittest.TestCase):
    def find_opposite(self, boolean_input):
        return not boolean_input
    def test_opposite_of_true(self):
        self.assertTrue(self.find_opposite(True))
    def test_opposite_of_false(self):
        self.assertFalse(self.find_opposite(False))
    def test_opposite_of_true_multiple(self):
        self.assertTrue(self.find_opposite(True))
    def test_opposite_of_false_multiple(self):
        self.assertFalse(self.find_opposite(False))
    def test_opposite_of_mixed_inputs(self):
        inputs = [True, False, True, False, True, False]
        expected_outputs = [False, True, False, True, False, True]
        for input_val, expected_val in zip(inputs, expected_outputs):
            with self.subTest(input=input_val):
                self.assertEqual(self.find_opposite(input_val), expected_val)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)