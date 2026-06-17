import unittest
def check_positive(value):
    return value > 0
class TestCheckPositive(unittest.TestCase):
    def test_integer_true(self):
        self.assertTrue(check_positive(5))
    def test_float_true(self):
        self.assertTrue(check_positive(3.14))
    def test_zero_false(self):
        self.assertFalse(check_positive(0))
    def test_negative_int_false(self):
        self.assertFalse(check_positive(-10))
    def test_negative_float_false(self):
        self.assertFalse(check_positive(-2.5))
if __name__ == '__main__':
    unittest.main()