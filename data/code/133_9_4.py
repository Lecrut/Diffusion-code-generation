import unittest
def evaluate_statement(statement):
    if not statement:
        return False
    statement = statement.strip()
    if statement == "true":
        return True
    elif statement == "false":
        return False
    else:
        return None
class TestEvaluateStatement(unittest.TestCase):
    def test_true_input(self):
        self.assertTrue(evaluate_statement("true"))
    def test_false_input(self):
        self.assertFalse(evaluate_statement("false"))
    def test_case_insensitivity(self):
        self.assertTrue(evaluate_statement("True"))
        self.assertFalse(evaluate_statement("False"))
    def test_whitespace_handling(self):
        self.assertTrue(evaluate_statement("  true  "))
        self.assertFalse(evaluate_statement("  false  "))
        self.assertFalse(evaluate_statement("  false "))
    def test_empty_string(self):
        self.assertFalse(evaluate_statement(""))
    def test_empty_string_with_whitespace(self):
        self.assertFalse(evaluate_statement("   "))
    def test_misspelled_true(self):
        self.assertIsNone(evaluate_statement("tru"))
        self.assertIsNone(evaluate_statement("truu"))
    def test_misspelled_false(self):
        self.assertIsNone(evaluate_statement("false"))
        self.assertIsNone(evaluate_statement("fals"))
    def test_other_strings(self):
        self.assertIsNone(evaluate_statement("yes"))
        self.assertIsNone(evaluate_statement("no"))
        self.assertIsNone(evaluate_statement("1"))
        self.assertIsNone(evaluate_statement("t"))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)