import unittest

def is_larger(a, b):
    return a > b

class TestIsLarger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_larger(10, 5))
        self.assertFalse(is_larger(5, 10))

    def test_negative_numbers(self):
        self.assertTrue(is_larger(-3, -5))
        self.assertFalse(is_larger(-5, -3))

    def test_zero_and_positive(self):
        self.assertTrue(is_larger(0, -1))
        self.assertFalse(is_larger(-1, 0))

    def test_zero_and_negative(self):
        self.assertTrue(is_larger(1, 0))
        self.assertFalse(is_larger(0, 1))

    def test_equality(self):
        self.assertFalse(is_larger(5, 5))
        self.assertFalse(is_larger(-3, -3))

if __name__ == '__main__':
    print("Running tests...")
    unittest.main(argv=[''], exit=False)
    print("\nFunction call examples:")
    print("is_larger(10, 5):", is_larger(10, 5))
    print("is_larger(-3, -5):", is_larger(-3, -5))
    print("is_larger(0, 0):", is_larger(0, 0))