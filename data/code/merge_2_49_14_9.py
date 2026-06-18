import unittest
def check_positive_result(value):
    return isinstance(value, (int, float)) and value > 0
class TestCheckPositiveResult(unittest.TestCase):
    def test_integer_positive(self):
        self.assertTrue(check_positive_result(10))
        self.assertTrue(check_positive_result(-5) == False)
    def test_float_positive(self):
        self.assertTrue(check_positive_result(3.14))
        self.assertFalse(check_positive_result(-2.718))
    def test_zero_and_negative(self):
        self.assertFalse(check_positive_result(0))
        self.assertFalse(check_positive_result(-999))
if __name__ == '__main__':
    unittest.main()