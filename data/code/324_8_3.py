import unittest
class MultiplicationModule:
    def multiply(self, a, b):
        return a * b
class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.calculator = MultiplicationModule()
    def test_positive_numbers(self):
        self.assertEqual(self.calculator.multiply(5, 3), 15)
        self.assertEqual(self.calculator.multiply(10, 2), 20)
        self.assertEqual(self.calculator.multiply(1, 100), 100)
    def test_multiplying_by_zero(self):
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(123, 0), 0)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
    def test_negative_numbers(self):
        self.assertEqual(self.calculator.multiply(-5, 3), -15)
        self.assertEqual(self.calculator.multiply(5, -3), -15)
        self.assertEqual(self.calculator.multiply(-5, -3), 15)
    def test_mixed_signs(self):
        self.assertEqual(self.calculator.multiply(-10, 2), -20)
        self.assertEqual(self.calculator.multiply(10, -2), -20)
        self.assertEqual(self.calculator.multiply(-10, -2), 20)
    def test_large_numbers(self):
        self.assertEqual(self.calculator.multiply(1000, 500), 500000)
        self.assertEqual(self.calculator.multiply(-100, 200), -20000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)