import unittest
def add_numbers(a, b):
    return a + b
class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)
    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(10, -4), 6)
    def test_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)
        self.assertEqual(add_numbers(-2, 0), -2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)