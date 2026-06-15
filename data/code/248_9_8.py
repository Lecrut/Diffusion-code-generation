import unittest
class AdditionCalculator:
    def add(self, a, b):
        return a + b
class TestAdditionCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = AdditionCalculator()
    def test_positive_numbers(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(10, 20), 30)
        self.assertEqual(self.calculator.add(1, 1), 2)
    def test_negative_numbers(self):
        self.assertEqual(self.calculator.add(-5, -3), -8)
        self.assertEqual(self.calculator.add(-10, 5), -5)
        self.assertEqual(self.calculator.add(10, -5), 5)
    def test_mixed_numbers(self):
        self.assertEqual(self.calculator.add(10, -5), 5)
        self.assertEqual(self.calculator.add(-10, 5), -5)
        self.assertEqual(self.calculator.add(-10, -5), -15)
    def test_zero_involvement(self):
        self.assertEqual(self.calculator.add(0, 5), 5)
        self.assertEqual(self.calculator.add(5, 0), 5)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-7, 0), -7)
    def test_large_numbers(self):
        self.assertEqual(self.calculator.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calculator.add(-500000, 1000000), 500000)
    def test_single_number_addition(self):
        self.assertEqual(self.calculator.add(10, 0), 10)
        self.assertEqual(self.calculator.add(0, 10), 10)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)