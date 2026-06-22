import unittest

def check_comparison(a, b):
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(10, 5))
        self.assertFalse(check_comparison(5, 10))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-5, -10))
        self.assertFalse(check_comparison(-10, -5))

    def test_mixed_signs(self):
        self.assertTrue(check_comparison(5, -10))
        self.assertFalse(check_comparison(-5, 10))

    def test_zero_values(self):
        self.assertFalse(check_comparison(0, 0))
        self.assertTrue(check_comparison(0, -1))
        self.assertFalse(check_comparison(-1, 0))

    def test_large_numbers(self):
        self.assertTrue(check_comparison(10 ** 9, 10 ** 8))
        self.assertFalse(check_comparison(10 ** 8, 10 ** 9))
if __name__ == '__main__':
    print(check_comparison(10, 5))
    print(check_comparison(-5, -10))
    print(check_comparison(0, 0))
    unittest.main(argv=[''], exit=False)