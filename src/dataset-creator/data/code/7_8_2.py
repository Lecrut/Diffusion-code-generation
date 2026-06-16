import unittest
class TruthEvaluator:
    def evaluate_statement(self, statement):
        if isinstance(statement, str) and not any(c.isdigit() for c in statement.strip()):
            return True if "true" in statement.lower() else False
        elif isinstance(statement, bool):
            return statement
        elif isinstance(statement, (int, float)):
            return self.evaluate_statement(str(bool(int(float(statement)))))
        else:
            raise TypeError(f"Unsupported input type for evaluation: {type(statement)}")
class TestTruthEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = TruthEvaluator()
    def test_true_string(self):
        result = self.evaluator.evaluate_statement("true is correct")
        self.assertTrue(result)
    def test_false_string(self):
        result = self.evaluator.evaluate_statement("false is incorrect")
        self.assertFalse(result)
    def test_boolean_input(self):
        self.assertEqual(True, self.evaluator.evaluate_statement(True))
        self.assertEqual(False, self.evaluator.evaluate_statement(False))
    def test_numeric_conversion(self):
        self.assertTrue(self.evaluator.evaluate_statement(1))
        self.assertFalse(self.evaluator.evaluate_statement(-1))
        self.assertTrue(self.evaluator.evaluate_statement(float("0.5")))
    def test_case_insensitivity(self):
        result = self.evaluator.evaluate_statement("TRUE")
        self.assertTrue(result)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTruthEvaluator)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)