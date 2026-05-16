import unittest
def is_zero(number):
    return number == 0
class TestIsZero(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_zero(0))
    def test_positive_number(self):
        self.assertFalse(is_zero(5))
    def test_negative_number(self):
        self.assertFalse(is_zero(-3))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)