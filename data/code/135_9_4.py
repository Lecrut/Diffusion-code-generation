import unittest
def check_equivalence(formula1, formula2):
    return formula1 == formula2
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology(self):
        formula1 = "(P OR NOT P)"
        formula2 = "TRUE"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology check failed")
        formula3 = "(P OR Q) AND (NOT (P OR Q))"
        formula4 = "FALSE"
        self.assertTrue(check_equivalence(formula3, formula4), "Contradiction check failed")
    def test_contradiction(self):
        formula1 = "(P AND NOT P)"
        formula2 = "FALSE"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction check failed")
        formula3 = "(P OR Q) AND (NOT P AND NOT Q)"
        formula4 = "FALSE"
        self.assertTrue(check_equivalence(formula3, formula4), "Contradiction check failed")
    def test_standard_equivalences(self):
        formula1 = "(NOT P OR Q)"
        formula2 = "(NOT P OR Q)"
        self.assertTrue(check_equivalence(formula1, formula2), "Implication equivalence failed")
        formula1 = "(NOT (P AND Q))"
        formula2 = "(NOT P OR NOT Q)"
        self.assertTrue(check_equivalence(formula1, formula2), "De Morgan's Law failed")
        formula1 = "(NOT (NOT P))"
        formula2 = "P"
        self.assertTrue(check_equivalence(formula1, formula2), "Double Negation failed")
        formula1 = "(P OR Q)"
        formula2 = "(Q OR P)"
        self.assertTrue(check_equivalence(formula1, formula2), "Commutativity failed")
        formula1 = "(P OR (Q OR R))"
        formula2 = "((P OR Q) OR R)"
        self.assertTrue(check_equivalence(formula1, formula2), "Associativity failed")
        formula1 = "(P AND (Q OR R))"
        formula2 = "((P AND Q) OR (P AND R))"
        self.assertTrue(check_equivalence(formula1, formula2), "Distributivity failed")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)