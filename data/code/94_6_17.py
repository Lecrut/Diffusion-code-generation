import unittest

class BooleanListEvaluator:
    def evaluate(self, boolean_list):
        return any(boolean_list)

class TestBooleanListEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = BooleanListEvaluator()

    def test_empty_list(self):
        result = self.evaluator.evaluate([])
        self.assertFalse(result)

    def test_all_false(self):
        result = self.evaluator.evaluate([False, False, False])
        self.assertFalse(result)

    def test_mixed_true(self):
        result = self.evaluator.evaluate([False, True, False])
        self.assertTrue(result)

    def test_all_true(self):
        result = self.evaluator.evaluate([True, True, True])
        self.assertTrue(result)

    def test_single_true(self):
        result = self.evaluator.evaluate([True])
        self.assertTrue(result)

    def test_single_false(self):
        result = self.evaluator.evaluate([False])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)