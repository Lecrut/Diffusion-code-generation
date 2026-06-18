import unittest
def check_positive_result(value):
    return value > 0
class TestCheckPositiveResult(unittest.TestCase):
    def test_integer_positive(self):
        self.assertTrue(check_positive_result(5))
    def test_integer_negative(self):
        self.assertFalse(check_positive_result(-3))
    def test_float_positive(self):
        self.assertTrue(check_positive_result(2.5))
    def test_float_zero(self):
        self.assertFalse(check_positive_result(0.0))
    def test_large_number(self):
        self.assertTrue(check_positive_result(1e10))
if __name__ == '__main__':
    unittest.main()