import unittest
def multiply(a, b):
    return a * b
class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 4), 20)
    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(4, -5), -20)
        self.assertEqual(multiply(-4, -5), 20)
    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
    def test_large_numbers(self):
        self.assertEqual(multiply(100, 200), 20000)
        self.assertEqual(multiply(-10, 50), -500)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)