import unittest
def evaluate_statement(statement):
    if not statement:
        return False
    return statement.lower() == "true"
class TestEvaluateStatement(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(evaluate_statement("True"))
        self.assertTrue(evaluate_statement("true"))
        self.assertTrue(evaluate_statement("TRUE"))
        self.assertTrue(evaluate_statement("  true  "))
    def test_false_cases(self):
        self.assertFalse(evaluate_statement("False"))
        self.assertFalse(evaluate_statement("false"))
        self.assertFalse(evaluate_statement("FALSE"))
        self.assertFalse(evaluate_statement("  false  "))
    def test_edge_cases(self):
        self.assertFalse(evaluate_statement(""))
        self.assertFalse(evaluate_statement(" "))
        self.assertFalse(evaluate_statement("fals"))
    def test_misspelled_inputs(self):
        self.assertFalse(evaluate_statement("tru"))
        self.assertFalse(evaluate_statement("fals e"))
        self.assertFalse(evaluate_statement("truue"))
        self.assertFalse(evaluate_statement("t"))
        self.assertFalse(evaluate_statement("yes"))
        self.assertFalse(evaluate_statement("no"))
        self.assertFalse(evaluate_statement("1"))
        self.assertFalse(evaluate_statement("abc"))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)