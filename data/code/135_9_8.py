import unittest
def check_equivalence(expr1, expr2):
    if expr1 == expr2:
        return True
    return False
class TestEquivalenceChecker(unittest.TestCase):
    def test_tautology(self):
        self.assertTrue(check_equivalence("P or not P", "True"))
        self.assertTrue(check_equivalence("(P or Q) or not (P or Q)", "True"))
    def test_contradiction(self):
        self.assertTrue(check_equivalence("P and not P", "False"))
        self.assertTrue(check_equivalence("P and not P", "False"))
    def test_standard_equivalences(self):
        self.assertTrue(check_equivalence("P -> Q", "not P or Q"))
        self.assertTrue(check_equivalence("(not P or Q)", "P -> Q"))
        self.assertTrue(check_equivalence("not (P and Q)", "not P or not Q"))
        self.assertTrue(check_equivalence("not (not P or not Q)", "P and Q"))
        self.assertTrue(check_equivalence("not (not P)", "P"))
        self.assertTrue(check_equivalence("P or Q", "Q or P"))
        self.assertTrue(check_equivalence("P and Q", "Q and P"))
        self.assertTrue(check_equivalence("(P or Q) or R", "P or (Q or R)"))
        self.assertTrue(check_equivalence("(P and Q) and R", "P and (Q and R)"))
        self.assertTrue(check_equivalence("P and (Q or R)", "(P and Q) or (P and R)"))
        self.assertTrue(check_equivalence("P or (Q and R)", "(P or Q) and (P or R)"))
    def test_identity_laws(self):
        self.assertTrue(check_equivalence("P or False", "P"))
        self.assertTrue(check_equivalence("False or P", "P"))
        self.assertTrue(check_equivalence("P and True", "P"))
        self.assertTrue(check_equivalence("True and P", "P"))
    def test_contradiction_laws(self):
        self.assertTrue(check_equivalence("P or False", "not (P and not False)"))
        self.assertTrue(check_equivalence("False or P", "not (not P and not False)"))
        self.assertTrue(check_equivalence("P and False", "False"))
        self.assertTrue(check_equivalence("False and P", "False"))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)