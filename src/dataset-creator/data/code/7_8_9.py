import unittest
class TestIntegerEquality(unittest.TestCase):
    def compare_integers(self, a, b):
        return a == b
    def test_equal_positive(self):
        self.assertTrue(self.compare_integers(5, 5))
        self.assertTrue(self.compare_integers(100, 100))
    def test_equal_negative(self):
        self.assertTrue(self.compare_integers(-10, -10))
        self.assertTrue(self.compare_integers(-50, -50))
    def test_unequal_positive(self):
        self.assertFalse(self.compare_integers(5, 6))
        self.assertFalse(self.compare_integers(10, 20))
    def test_unequal_mixed(self):
        self.assertFalse(self.compare_integers(1, 2))
        self.assertFalse(self.compare_integers(-5, 5))
    def test_equal_zero(self):
        self.assertTrue(self.compare_integers(0, 0))
    def test_unequal_with_zero(self):
        self.assertFalse(self.compare_integers(0, 1))
        self.assertFalse(self.compare_integers(-5, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)