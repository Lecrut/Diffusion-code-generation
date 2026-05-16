import unittest
def verify_boolean_equivalence(a, b, c):
    return (a == b) == (a == c)
class TestBooleanEquivalence(unittest.TestCase):
    def test_basic_equivalence(self):
        self.assertTrue(verify_boolean_equivalence(True, True, True))
        self.assertTrue(verify_boolean_equivalence(False, False, False))
        self.assertFalse(verify_boolean_equivalence(True, False, True))
        self.assertFalse(verify_boolean_equivalence(True, True, False))
    def test_mixed_equivalence(self):
        self.assertTrue(verify_boolean_equivalence(True, True, False))
        self.assertFalse(verify_boolean_equivalence(False, True, True))
        self.assertFalse(verify_boolean_equivalence(False, False, True))
        self.assertTrue(verify_boolean_equivalence(True, False, False))
    def test_edge_case_all_false(self):
        self.assertTrue(verify_boolean_equivalence(False, False, False))
    def test_edge_case_all_true(self):
        self.assertTrue(verify_boolean_equivalence(True, True, True))
    def test_two_equal_one_different(self):
        self.assertFalse(verify_boolean_equivalence(True, True, False))
        self.assertFalse(verify_boolean_equivalence(False, False, True))
    def test_complex_scenarios(self):
        self.assertTrue(verify_boolean_equivalence(True, True, True))
        self.assertTrue(verify_boolean_equivalence(False, False, False))
        self.assertTrue(verify_boolean_equivalence(True, True, False))
        self.assertTrue(verify_boolean_equivalence(True, False, False))
        self.assertTrue(verify_boolean_equivalence(False, True, True))
        self.assertTrue(verify_boolean_equivalence(False, True, False))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)