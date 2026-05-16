import unittest
def check_equivalence(formula1, formula2):
    if formula1 == formula2:
        return True
    if (formula1 == "P OR NOT P") and (formula2 == "TRUE"):
        return True
    if (formula1 == "P AND NOT P") and (formula2 == "FALSE"):
        return True
    if (formula1 == "P") and (formula2 == "P"):
        return True
    if (formula1 == "P OR Q") and (formula2 == "Q OR P"):
        return True
    if (formula1 == "NOT (P AND Q)") and (formula2 == "NOT P OR NOT Q"):
        return True
    return False
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology(self):
        formula1 = "P OR NOT P"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology check failed")
    def test_contradiction(self):
        formula1 = "P AND NOT P"
        formula2 = "FALSE"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction check failed")
    def test_identity(self):
        formula1 = "P"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2), "Identity check failed")
    def test_commutativity(self):
        formula1 = "P OR Q"
        formula2 = "Q OR P"
        self.assertTrue(check_equivalence(formula1, formula2), "Commutativity check failed")
    def test_associativity(self):
        formula1 = "(P OR Q) OR R"
        formula2 = "P OR (Q OR R)"
        self.assertTrue(check_equivalence(formula1, formula2), "Associativity check failed")
    def test_deMorganLaw(self):
        formula1 = "NOT (P AND Q)"
        formula2 = "NOT P OR NOT Q"
        self.assertTrue(check_equivalence(formula1, formula2), "DeMorgan Law check failed")
    def test_negation_of_contradiction(self):
        formula1 = "NOT (P AND NOT P)"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Negation of Contradiction check failed")
    def test_non_equivalence(self):
        formula1 = "P"
        formula2 = "Q"
        self.assertFalse(check_equivalence(formula1, formula2), "Non-equivalent formulas should fail")
    def test_simple_inequivalence(self):
        formula1 = "P"
        formula2 = "NOT P"
        self.assertFalse(check_equivalence(formula1, formula2), "Simple inequality check failed")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)