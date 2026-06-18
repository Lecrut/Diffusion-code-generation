import unittest
class TruthEvaluator:
    def evaluate_statement(self, statement):
        if not isinstance(statement, str) or len(statement.strip()) == 0:
            return False
        stripped = statement.lower().strip()
        if stripped in ['true', 'yes']:
            return True
        elif stripped in ['false', 'no']:
            return False
        try:
            result = eval(stripped, {"__builtins__": {}}, {})
            if isinstance(result, bool):
                return result
            elif isinstance(result, int | float):
                return True
            else:
                raise ValueError("Non-numeric non-boolean expression")
        except Exception:
            return False
class TestTruthEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = TruthEvaluator()
    def test_explicit_true(self):
        assert self.evaluator.evaluate_statement("true") is True
        assert self.evaluator.evaluate_statement("yes") is True
    def test_explicit_false(self):
        assert self.evaluator.evaluate_statement("false") is False
        assert self.evaluator.evaluate_statement("no") is False
    def test_mathematical_expressions_true(self):
        assert self.evaluator.evaluate_statement("2+2==4") is True
        assert self.evaluator.evaluate_statement("(10-5)==5") is True
    def test_mathematical_expressions_false(self):
        assert self.evaluator.evaluate_statement("2+2==5") is False
        assert self.evaluator.evaluate_statement("3*3>9") is False
    def test_invalid_inputs(self):
        assert self.evaluator.evaluate_statement("") is False
        assert self.evaluator.evaluate_statement(None) is False
if __name__ == '__main__':
    unittest.main()