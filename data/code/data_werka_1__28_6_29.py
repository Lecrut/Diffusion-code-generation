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

    def test_mixed_signs(self):
        self.assertTrue(is_larger(5, -10))
        self.assertFalse(is_larger(-5, 10))

    def test_equal_numbers(self):
        self.assertFalse(is_larger(5, 5))
if __name__ == '__main__':
    print('Test results:')
    unittest.main(argv=[''], exit=False)
    a = 7
    b = 3
    result = is_larger(a, b)
    print(f'is_larger({a}, {b}) = {result}')
    a = -2
    b = -5
    result = is_larger(a, b)
    print(f'is_larger({a}, {b}) = {result}')
    a = 4
    b = 4
    result = is_larger(a, b)
    print(f'is_larger({a}, {b}) = {result}')