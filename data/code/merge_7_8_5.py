import unittest
class TestIntegerEquality(unittest.TestCase):
    def compare_integers(self, a, b):
        return a == b
    def test_equal_numbers(self):
        self.assertTrue(self.compare_integers(5, 5))
        self.assertTrue(self.compare_integers(-10, -10))
        self.assertTrue(self.compare_integers(0, 0))
    def test_unequal_numbers(self):
        self.assertFalse(self.compare_integers(5, 6))
        self.assertFalse(self.compare_integers(10, 20))
        self.assertFalse(self.compare_integers(-5, 5))
    def test_mixed_signs(self):
        self.assertFalse(self.compare_integers(1, -1))
        self.assertFalse(self.compare_integers(-10, 10))
    def test_zero_comparison(self):
        self.assertTrue(self.compare_integers(0, 0))
        self.assertFalse(self.compare_integers(0, 1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)