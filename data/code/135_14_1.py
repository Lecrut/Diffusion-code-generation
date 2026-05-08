import unittest
def verify_boolean_equivalence(a, b):
    return (a == b)
class TestBooleanEquivalence(unittest.TestCase):
    def test_true_equivalence(self):
        self.assertTrue(verify_boolean_equivalence(True, True))
        self.assertTrue(verify_boolean_equivalence(False, False))
    def test_false_equivalence(self):
        self.assertFalse(verify_boolean_equivalence(True, False))
        self.assertFalse(verify_boolean_equivalence(False, True))
    def test_mixed_equivalence(self):
        self.assertTrue(verify_boolean_equivalence(True, True))
        self.assertFalse(verify_boolean_equivalence(True, False))
        self.assertFalse(verify_boolean_equivalence(False, True))
        self.assertTrue(verify_boolean_equivalence(False, False))
    def test_edge_case_zero_and_one(self):
        self.assertTrue(verify_boolean_equivalence(1, 1))
        self.assertTrue(verify_boolean_equivalence(0, 0))
        self.assertFalse(verify_boolean_equivalence(1, 0))
        self.assertFalse(verify_boolean_equivalence(0, 1))
    def test_complex_combinations(self):
        self.assertTrue(verify_boolean_equivalence(True, True))
        self.assertTrue(verify_boolean_equivalence(False, False))
        self.assertFalse(verify_boolean_equivalence(True, False))
        self.assertFalse(verify_boolean_equivalence(False, True))
    def test_mixed_types(self):
        self.assertTrue(verify_boolean_equivalence(1, True))
        self.assertFalse(verify_boolean_equivalence(0, False))
        self.assertFalse(verify_boolean_equivalence(1, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)