import unittest
class TrueFalseEvaluator:
    def evaluate_statement(self, statement):
        return bool(eval(statement)) if isinstance(statement, str) else False
    def get_evaluation_result(self, expression):
        try:
            result = eval(expression)
            is_true_false = isinstance(result, (bool, int)) and not isinstance(result, complex) or isinstance(result, bool)
            if is_true_false:
                return {
                    "expression": str(expression),
                    "result": result,
                    "is_valid_statement": True,
                    "message": f"Statement '{str(expression)}' evaluates to {'True' if result else 'False'}."
                }
            elif isinstance(result, (list, tuple)):
                return {
                    "expression": str(expression),
                    "result": list(result) if isinstance(result, tuple) else result,
                    "is_valid_statement": True,
                    "message": f"Expression '{str(expression)}' evaluates to a collection."
                }
            else:
                return {
                    "expression": str(expression),
                    "result": None,
                    "is_valid_statement": False,
                    "message": f"'{str(expression)}' is not a simple true/false statement or returns an invalid type."
                }
        except Exception as e:
            return {
                "expression": str(expression),
                "error": str(e),
                "result": None,
                "is_valid_statement": False,
                "message": f"Error evaluating '{str(expression)}': {e}"
            }
class TestTrueFalseEvaluator(unittest.TestCase):
    def test_simple_true(self):
        evaluator = TrueFalseEvaluator()
        result = evaluator.get_evaluation_result("2 + 1 == 3")
        self.assertEqual(result["result"], True)
        self.assertTrue(result["is_valid_statement"])
    def test_simple_false(self):
        evaluator = TrueFalseEvaluator()
        result = evaluator.get_evaluation_result("5 > 4")
        self.assertEqual(result["result"], False)
        self.assertFalse(result["is_valid_statement"])
    def test_invalid_expression(self):
        evaluator = TrueFalseEvaluator()
        result = evaluator.get_evaluation_result("[1, 2]")
        self.assertTrue(result["error"] is not None or "list" in str(result).lower())
    def test_boolean_directly(self):
        evaluator = TrueFalseEvaluator()
        result = evaluator.evaluate_statement(True)
        self.assertEqual(result, True)
if __name__ == '__main__':
    unittest.main(exit=False)