import unittest
class TestProductFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(product(5, 3), 15)
    def test_negative_numbers(self):
        self.assertEqual(product(-5, 3), -15)
        self.assertEqual(product(-5, -3), 15)
    def test_zero_involvement(self):
        self.assertEqual(product(10, 0), 0)
        self.assertEqual(product(0, -5), 0)
        self.assertEqual(product(0, 0), 0)
    def test_mixed_signs(self):
        self.assertEqual(product(5, -3), -15)
        self.assertEqual(product(-5, -3), 15)
    def test_large_numbers(self):
        self.assertEqual(product(100, 200), 20000)
def product(a, b):
    return a * b
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)