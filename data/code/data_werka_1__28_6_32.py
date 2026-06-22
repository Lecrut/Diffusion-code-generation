import unittest

def is_larger(value1, value2):
    return value1 > value2

class TestIsLarger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_larger(10, 5))
        self.assertFalse(is_larger(5, 10))

    def test_negative_numbers(self):
        self.assertTrue(is_larger(-5, -10))
        self.assertFalse(is_larger(-10, -5))

    def test_mixed_signs(self):
        self.assertTrue(is_larger(5, -10))
        self.assertFalse(is_larger(-5, 10))

    def test_zero_values(self):
        self.assertFalse(is_larger(0, 0))
        self.assertFalse(is_larger(0, -1))
        self.assertTrue(is_larger(0, -2))

    def test_large_numbers(self):
        self.assertTrue(is_larger(10 ** 9, 10 ** 8))
        self.assertFalse(is_larger(10 ** 8, 10 ** 9))
if __name__ == '__main__':
    print('Testing is_larger function:')
    unittest.main(argv=[''], exit=False)
    print('is_larger(10, 5):', is_larger(10, 5))
    print('is_larger(-5, -10):', is_larger(-5, -10))
    print('is_larger(0, 0):', is_larger(0, 0))
    print('is_larger(10**9, 10**8):', is_larger(10 ** 9, 10 ** 8))