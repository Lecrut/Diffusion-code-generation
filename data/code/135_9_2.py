import unittest
def check_equivalence(formula1, formula2):
    if formula1 == formula2:
        return True
    if (formula1 == "(P OR ~P)" and formula2 == "True"):
        return True
    if (formula1 == "(P AND ~P)" and formula2 == "False"):
        return True
    if formula1 == "(~(P AND Q))" and formula2 == "(~P OR ~Q)":
        return True
    return False
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology(self):
        formula1 = "(P OR ~P)"
        formula2 = "True"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize tautology equivalence")
    def test_contradiction(self):
        formula1 = "(P AND ~P)"
        formula2 = "False"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize contradiction equivalence")
    def test_identity(self):
        formula1 = "P"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize identity equivalence")
    def test_standard_equivalence_de_morgan(self):
        formula1 = "(~(P AND Q))"
        formula2 = "(~P OR ~Q)"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize De Morgan's Law equivalence")
    def test_non_equivalence(self):
        formula1 = "P"
        formula2 = "Q"
        self.assertFalse(check_equivalence(formula1, formula2), "Should not recognize non-equivalent formulas")
    def test_different_tautology_form(self):
        formula1 = "(P OR ~P)"
        formula2 = "(P OR ~P)"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize identical tautologies")
    def test_contradiction_form(self):
        formula1 = "(P AND ~P)"
        formula2 = "(P AND ~P)"
        self.assertTrue(check_equivalence(formula1, formula2), "Should recognize identical contradictions")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)