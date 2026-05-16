import unittest
def verify_equivalence(a, b, c):
    return (a == b) == (a == c)
class TestEquivalenceVerification(unittest.TestCase):
    def test_basic_equivalence(self):
        self.assertTrue(verify_equivalence(True, True, True))
        self.assertTrue(verify_equivalence(False, False, False))
        self.assertFalse(verify_equivalence(True, False, True))
        self.assertFalse(verify_equivalence(True, True, False))
        self.assertFalse(verify_equivalence(False, True, True))
        self.assertTrue(verify_equivalence(False, False, True))
    def test_mixed_values(self):
        self.assertTrue(verify_equivalence(1, 1, 1))
        self.assertTrue(verify_equivalence(1, 1, 2))
        self.assertFalse(verify_equivalence(1, 2, 1))
        self.assertFalse(verify_equivalence(1, 2, 3))
        self.assertTrue(verify_equivalence(0, 0, 0))
        self.assertTrue(verify_equivalence(0, 0, 1))
        self.assertFalse(verify_equivalence(0, 1, 0))
        self.assertFalse(verify_equivalence(0, 1, 2))
    def test_boolean_edge_cases(self):
        self.assertTrue(verify_equivalence(True, True, False))
        self.assertFalse(verify_equivalence(True, False, False))
        self.assertFalse(verify_equivalence(False, True, False))
        self.assertTrue(verify_equivalence(False, False, True))
    def test_large_numbers(self):
        self.assertTrue(verify_equivalence(100, 100, 100))
        self.assertTrue(verify_equivalence(50, 50, 50))
        self.assertFalse(verify_equivalence(100, 100, 101))
        self.assertFalse(verify_equivalence(100, 101, 100))
        self.assertTrue(verify_equivalence(1000, 1000, 1000))
        self.assertTrue(verify_equivalence(1000, 1000, 10000))
        self.assertFalse(verify_equivalence(1000, 10000, 1000))
    def test_zero_and_one(self):
        self.assertTrue(verify_equivalence(0, 0, 0))
        self.assertTrue(verify_equivalence(1, 1, 1))
        self.assertFalse(verify_equivalence(0, 1, 0))
        self.assertFalse(verify_equivalence(1, 0, 1))
        self.assertFalse(verify_equivalence(0, 1, 1))
        self.assertFalse(verify_equivalence(1, 0, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)