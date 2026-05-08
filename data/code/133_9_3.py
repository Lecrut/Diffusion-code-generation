import unittest
def evaluate_statement(statement):
    if not statement:
        return False
    return statement.lower() == "true"
class TestEvaluateStatement(unittest.TestCase):
    def test_true_case(self):
        self.assertTrue(evaluate_statement("True"))
        self.assertTrue(evaluate_statement("true"))
        self.assertTrue(evaluate_statement("TRUE"))
    def test_false_case(self):
        self.assertFalse(evaluate_statement("False"))
        self.assertFalse(evaluate_statement("false"))
        self.assertFalse(evaluate_statement("FALSE"))
    def test_mixed_case_false(self):
        self.assertFalse(evaluate_statement("No"))
        self.assertFalse(evaluate_statement("fAlSe"))
    def test_empty_string(self):
        self.assertFalse(evaluate_statement(""))
    def test_whitespace_only(self):
        self.assertFalse(evaluate_statement("  "))
        self.assertFalse(evaluate_statement("\t\n"))
    def test_misspelled_true(self):
        self.assertFalse(evaluate_statement("Tru"))
        self.assertFalse(evaluate_statement("tru"))
    def test_misspelled_false(self):
        self.assertFalse(evaluate_statement("Fals"))
        self.assertFalse(evaluate_statement("falSe"))
    def test_non_boolean_strings(self):
        self.assertFalse(evaluate_statement("yes"))
        self.assertFalse(evaluate_statement("no"))
        self.assertFalse(evaluate_statement("1"))
        self.assertFalse(evaluate_statement("0"))
        self.assertFalse(evaluate_statement("anything"))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)