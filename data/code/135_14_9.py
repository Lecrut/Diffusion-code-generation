import unittest
def verify_equivalence(a, b, c):
    return (a == b) == (a == c)
class TestEquivalenceVerification(unittest.TestCase):
    def test_basic_equivalence(self):
        self.assertTrue(verify_equivalence(True, True, True))
        self.assertTrue(verify_equivalence(False, False, False))
        self.assertTrue(verify_equivalence(True, True, False))
        self.assertFalse(verify_equivalence(True, False, True))
        self.assertFalse(verify_equivalence(False, True, True))
        self.assertTrue(verify_equivalence(False, False, True))
    def test_mixed_values(self):
        self.assertTrue(verify_equivalence(1, 1, 1))
        self.assertTrue(verify_equivalence(1, 1, 0))
        self.assertFalse(verify_equivalence(1, 0, 1))
        self.assertFalse(verify_equivalence(0, 1, 1))
        self.assertTrue(verify_equivalence(0, 0, 1))
    def test_edge_cases_with_none(self):
        self.assertTrue(verify_equivalence(None, None, None))
        self.assertTrue(verify_equivalence(None, None, None))
        self.assertTrue(verify_equivalence(None, None, None))
        self.assertTrue(verify_equivalence(None, None, None))
    def test_mixed_boolean_and_int(self):
        self.assertTrue(verify_equivalence(True, 1, True))
        self.assertTrue(verify_equivalence(False, 0, False))
        self.assertTrue(verify_equivalence(True, False, False))
        self.assertFalse(verify_equivalence(True, True, False))
        self.assertFalse(verify_equivalence(False, False, True))
    def test_complex_logic(self):
        self.assertTrue(verify_equivalence(True, True, True))
        self.assertTrue(verify_equivalence(False, False, False))
        self.assertTrue(verify_equivalence(True, True, False))
        self.assertFalse(verify_equivalence(True, False, True))
        self.assertFalse(verify_equivalence(False, True, True))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)