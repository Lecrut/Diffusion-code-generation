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

    def test_zero_and_positive_number(self):
        self.assertTrue(is_larger(0, -1))
        self.assertFalse(is_larger(-1, 0))

    def test_zero_and_negative_number(self):
        self.assertTrue(is_larger(1, 0))
        self.assertFalse(is_larger(0, 1))

    def test_equal_numbers(self):
        self.assertFalse(is_larger(7, 7))
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(-3, -10))
    print(is_larger(0, 0))
    unittest.main(argv=[''], exit=False)