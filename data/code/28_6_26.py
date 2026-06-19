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

    def test_zero_and_positive(self):
        self.assertTrue(is_larger(0, -1))
        self.assertFalse(is_larger(-1, 0))

    def test_zero_and_negative(self):
        self.assertFalse(is_larger(0, 1))
        self.assertTrue(is_larger(1, 0))

    def test_equal_numbers(self):
        self.assertFalse(is_larger(5, 5))
        self.assertFalse(is_larger(-5, -5))

if __name__ == '__main__':
    print("Testing is_larger function:")
    print(f"Is 10 larger than 5? {is_larger(10, 5)}")
    print(f"Is 5 larger than 10? {is_larger(5, 10)}")
    print(f"Is -5 larger than -10? {is_larger(-5, -10)}")
    print(f"Is -10 larger than -5? {is_larger(-10, -5)}")
    print(f"Is 0 larger than -1? {is_larger(0, -1)}")
    print(f"Is -1 larger than 0? {is_larger(-1, 0)}")
    print(f"Is 5 larger than 5? {is_larger(5, 5)}")
    print(f"Is -5 larger than -5? {is_larger(-5, -5)}")

    unittest.main(argv=[''], exit=False)