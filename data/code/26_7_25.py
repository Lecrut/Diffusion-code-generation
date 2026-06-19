import unittest

def check_comparison(a, b):
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(2, 4))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-1, -3))
        self.assertFalse(check_comparison(-2, -2))
        self.assertFalse(check_comparison(-4, -1))

    def test_zero_and_positive(self):
        self.assertTrue(check_comparison(0, -1))
        self.assertFalse(check_comparison(0, 1))

    def test_zero_and_negative(self):
        self.assertTrue(check_comparison(-1, 0))
        self.assertFalse(check_comparison(1, 0))

    def test_equal_numbers(self):
        self.assertFalse(check_comparison(3, 3))
        self.assertFalse(check_comparison(-2, -2))
if __name__ == '__main__':
    print(check_comparison(5, 3))
    print(check_comparison(-1, -3))
    print(check_comparison(0, 0))
    unittest.main(argv=[''], exit=False)