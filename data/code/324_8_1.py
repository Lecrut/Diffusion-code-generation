import unittest
class MultiplicationFunctions:
    def multiply(self, a, b):
        return a * b
class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.calc = MultiplicationFunctions()
    def test_positive_numbers(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 4), 40)
        self.assertEqual(self.calc.multiply(1, 100), 100)
    def test_multiplying_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(123, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
    def test_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
    def test_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-4, 2), -8)
        self.assertEqual(self.calc.multiply(4, -2), -8)
        self.assertEqual(self.calc.multiply(-10, -5), 50)
    def test_large_numbers(self):
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)
        self.assertEqual(self.calc.multiply(-99, 100), -9900)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)