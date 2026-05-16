import unittest
def check_equivalence(formula1, formula2):
    return formula1 == formula2
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology(self):
        formula1 = "(P OR NOT P)"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology check failed")
    def test_contradiction(self):
        formula1 = "(P AND NOT P)"
        formula2 = "FALSE"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction check failed")
    def test_standard_equivalence_implication(self):
        formula1 = "(NOT P OR Q)"
        formula2 = "(P IMPLIES Q)"
        self.assertTrue(check_equivalence(formula1, formula2), "Implication equivalence failed")
    def test_standard_equivalence_deMorgan(self):
        formula1 = "(NOT (P AND Q))"
        formula2 = "(NOT P OR NOT Q)"
        self.assertTrue(check_equivalence(formula1, formula2), "DeMorgan equivalence failed")
    def test_identity_law(self):
        formula1 = "P"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2), "Identity law failed")
    def test_commutative_law(self):
        formula1 = "(P OR Q)"
        formula2 = "(Q OR P)"
        self.assertTrue(check_equivalence(formula1, formula2), "Commutative law failed")
    def test_associative_law(self):
        formula1 = "(P OR (Q OR R))"
        formula2 = "((P OR Q) OR R)"
        self.assertTrue(check_equivalence(formula1, formula2), "Associative law failed")
    def test_distributive_law(self):
        formula1 = "(P AND (Q OR R))"
        formula2 = "((P AND Q) OR (P AND R))"
        self.assertTrue(check_equivalence(formula1, formula2), "Distributive law failed")
    def test_contradiction_equivalence(self):
        formula1 = "(P AND NOT P)"
        formula2 = "FALSE"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction to False failed")
    def test_tautology_equivalence(self):
        formula1 = "(P OR NOT P)"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology to True failed")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)