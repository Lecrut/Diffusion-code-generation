import unittest
def check_difference(a, b):
    return a != b
class TestNumberDifference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check_difference(5, 10))
        self.assertFalse(check_difference(5, 5))
    def test_negative_numbers(self):
        self.assertTrue(check_difference(-5, -10))
        self.assertFalse(check_difference(-5, -5))
        self.assertTrue(check_difference(-10, -5))
    def test_mixed_signs(self):
        self.assertTrue(check_difference(5, -5))
        self.assertFalse(check_difference(5, 5))
    def test_involving_zero(self):
        self.assertTrue(check_difference(0, 5))
        self.assertFalse(check_difference(0, 0))
        self.assertTrue(check_difference(-5, 0))
        self.assertTrue(check_difference(0, -5))
    def test_zero_difference(self):
        self.assertFalse(check_difference(0, 0))
    def test_floating_point_numbers(self):
        self.assertTrue(check_difference(1.5, 2.5))
        self.assertFalse(check_difference(1.5, 1.5))
        self.assertTrue(check_difference(0.0, 0.001))
        self.assertFalse(check_difference(3.14, 3.14))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)