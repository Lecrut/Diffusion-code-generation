import unittest
def multiply(a, b):
    return a * b
class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(10, 2), 20)
    def test_negative_numbers(self):
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(10, -2), -20)
        self.assertEqual(multiply(-5, -3), 15)
    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-10, 0), 0)
    def test_large_numbers(self):
        self.assertEqual(multiply(100, 50), 5000)
        self.assertEqual(multiply(-1000, 2000), -2000000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)