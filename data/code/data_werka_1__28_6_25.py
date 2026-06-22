import unittest

def is_larger(a, b):
    return a > b

class TestIsLarger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_larger(10, 5))
        self.assertFalse(is_larger(5, 10))

    def test_negative_numbers(self):
        self.assertTrue(is_larger(-5, -10))
        self.assertFalse(is_larger(-10, -5))

    def test_equal_numbers(self):
        self.assertFalse(is_larger(7, 7))

    def test_mixed_signs(self):
        self.assertTrue(is_larger(-1, 0))
        self.assertFalse(is_larger(0, -1))
if __name__ == '__main__':
    print('Testing with positive numbers:', is_larger(10, 5))
    print('Testing with negative numbers:', is_larger(-5, -10))
    print('Testing with equal numbers:', is_larger(7, 7))
    print('Testing with mixed signs:', is_larger(-1, 0))
    unittest.main(argv=[''], exit=False)