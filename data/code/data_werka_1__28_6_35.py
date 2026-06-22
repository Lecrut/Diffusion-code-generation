import unittest

def is_larger(a, b):
    return a > b

class TestIsLarger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_larger(10, 5))
        self.assertFalse(is_larger(5, 10))

    def test_negative_numbers(self):
        self.assertTrue(is_larger(-3, -10))
        self.assertFalse(is_larger(-10, -3))

    def test_equal_numbers(self):
        self.assertFalse(is_larger(7, 7))
        self.assertFalse(is_larger(-2, -2))

    def test_mixed_signs(self):
        self.assertTrue(is_larger(5, -10))
        self.assertFalse(is_larger(-5, 10))
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(5, 10))
    print(is_larger(-3, -10))
    print(is_larger(-10, -3))
    print(is_larger(7, 7))
    print(is_larger(-2, -2))
    print(is_larger(5, -10))
    print(is_larger(-5, 10))
    unittest.main()