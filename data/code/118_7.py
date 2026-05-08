import unittest
class MathFunctions:
    def multiply(self, a, b):
        return a * b
class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.math_functions = MathFunctions()
    def test_positive_numbers(self):
        self.assertEqual(self.math_functions.multiply(5, 3), 15)
        self.assertEqual(self.math_functions.multiply(10, 2), 20)
    def test_negative_numbers(self):
        self.assertEqual(self.math_functions.multiply(-5, 3), -15)
        self.assertEqual(self.math_functions.multiply(-4, -2), 8)
    def test_zero_involvement(self):
        self.assertEqual(self.math_functions.multiply(0, 5), 0)
        self.assertEqual(self.math_functions.multiply(-10, 0), 0)
    def test_mixed_signs(self):
        self.assertEqual(self.math_functions.multiply(5, -3), -15)
        self.assertEqual(self.math_functions.multiply(-5, -3), 15)
    def test_large_numbers(self):
        self.assertEqual(self.math_functions.multiply(100, 200), 20000)
        self.assertEqual(self.math_functions.multiply(-1000, 50), -50000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)