import unittest
def check_equivalence(formula1, formula2):
    return formula1 == formula2
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology_equivalence(self):
        formula1 = "P | ~P"
        formula2 = "True"
        self.assertTrue(check_equivalence(formula1, formula2), "Tautology equivalence failed")
        formula3 = "P | Q"
        formula4 = "P | Q"
        self.assertTrue(check_equivalence(formula3, formula4), "Identical tautologies failed")
    def test_contradiction_equivalence(self):
        formula1 = "P & ~P"
        formula2 = "False"
        self.assertTrue(check_equivalence(formula1, formula2), "Contradiction equivalence failed")
        formula3 = "P & ~P"
        formula4 = "False"
        self.assertTrue(check_equivalence(formula3, formula4), "Identical contradictions failed")
    def test_standard_equivalences(self):
        formula1 = "~(P & Q)"
        formula2 = "~P | ~Q"
        self.assertTrue(check_equivalence(formula1, formula2), "De Morgan's Law failed")
        formula3 = "P & (Q | R)"
        formula4 = "(P & Q) | (P & R)"
        self.assertTrue(check_equivalence(formula3, formula4), "Distributive Law failed")
        formula5 = "~~P"
        formula6 = "P"
        self.assertTrue(check_equivalence(formula5, formula6), "Double Negation failed")
        formula7 = "P -> Q"
        formula8 = "~P | Q"
        self.assertTrue(check_equivalence(formula7, formula8), "Implication Equivalence failed")
    def test_non_equivalence(self):
        formula1 = "P"
        formula2 = "~P"
        self.assertFalse(check_equivalence(formula1, formula2), "Simple negation failure")
        formula3 = "P | Q"
        formula4 = "R"
        self.assertFalse(check_equivalence(formula3, formula4), "Completely different formulas failed")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)