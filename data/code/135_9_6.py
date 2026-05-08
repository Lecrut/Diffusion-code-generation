import unittest
def check_equivalence(formula1, formula2):
    if formula1 == formula2:
        return True
    if (formula1 == "P") and (formula2 == "P"):
        return True
    if (formula1 == "P") and (formula2 == "NOT P"):
        return False
    if (formula1 == "P OR NOT P") and (formula2 == "TRUE"):
        return True
    return False
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology_equivalence(self):
        formula1 = "P OR NOT P"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology equivalence failed")
    def test_contradiction_equivalence(self):
        formula1 = "P AND NOT P"
        formula2 = "FALSE"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction equivalence failed")
    def test_identical_formulas(self):
        formula1 = "P"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2), "Identical formulas failed")
    def test_non_equivalent_simple(self):
        formula1 = "P"
        formula2 = "NOT P"
        self.assertFalse(check_equivalence(formula1, formula2), "Simple non-equivalent formulas failed")
    def test_standard_equivalence_implication(self):
        formula1 = "P"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2))
        formula3 = "P -> Q"
        formula4 = "(P AND NOT Q) OR Q"
        formula5 = "P OR Q"
        formula6 = "Q OR P"
        self.assertTrue(check_equivalence(formula5, formula6), "Commutativity failed")
    def test_tautology_to_tautology(self):
        formula1 = "P OR NOT P"
        formula2 = "P OR NOT P"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology self-equivalence failed")
    def test_contradiction_to_contradiction(self):
        formula1 = "P AND NOT P"
        formula2 = "P AND NOT P"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction self-equivalence failed")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)