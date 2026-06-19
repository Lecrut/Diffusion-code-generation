import unittest

def check_comparison(a, b):
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(10, 5))
        self.assertFalse(check_comparison(3, 7))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-2, -5))
        self.assertFalse(check_comparison(-8, -4))

    def test_mixed_signs(self):
        self.assertTrue(check_comparison(5, -10))
        self.assertFalse(check_comparison(-3, 2))

    def test_zero_values(self):
        self.assertFalse(check_comparison(0, 0))
        self.assertFalse(check_comparison(0, -1))
        self.assertTrue(check_comparison(0, -2))

    def test_large_numbers(self):
        self.assertTrue(check_comparison(10 ** 9, 10 ** 8))
        self.assertFalse(check_comparison(-10 ** 9, -10 ** 8))
if __name__ == '__main__':
    a = 7
    b = 3
    result = check_comparison(a, b)
    print(f'check_comparison({a}, {b}) = {result}')
    unittest.main(argv=[''], exit=False)