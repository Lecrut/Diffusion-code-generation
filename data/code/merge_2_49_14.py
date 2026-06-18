import unittest
def check_positive(value):
    return isinstance(value, (int, float)) and value > 0
class TestPositiveChecker(unittest.TestCase):
    def test_integer_positive(self):
        self.assertTrue(check_positive(5))
    def test_float_positive(self):
        self.assertTrue(check_positive(3.14))
    def test_zero(self):
        self.assertFalse(check_positive(0))
    def test_negative_int(self):
        self.assertFalse(check_positive(-10))
    def test_negative_float(self):
        self.assertFalse(check_positive(-2.5))
if __name__ == '__main__':
    unittest.main()