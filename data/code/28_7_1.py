import unittest
def is_larger(a, b):
    return a > b
class TestIsLarger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_larger(5, 3))
        self.assertFalse(is_larger(3, 5))
        self.assertFalse(is_larger(5, 5))
    def test_negative_numbers(self):
        self.assertTrue(is_larger(-1, -5))
        self.assertFalse(is_larger(-5, -1))
        self.assertFalse(is_larger(-5, -5))
    def test_mixed_numbers(self):
        self.assertTrue(is_larger(10, -2))
        self.assertFalse(is_larger(-10, 2))
        self.assertFalse(is_larger(-10, -20))
    def test_equality(self):
        self.assertFalse(is_larger(7, 7))
        self.assertFalse(is_larger(0, 0))
        self.assertFalse(is_larger(-3, -3))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)