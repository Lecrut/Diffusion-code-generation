import unittest
class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return weight1 - weight2
class TestWeightCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = WeightCalculator()
    def test_positive_difference(self):
        self.assertEqual(self.calculator.calculate_difference(10, 5), 5)
        self.assertEqual(self.calculator.calculate_difference(20, 10), 10)
    def test_zero_difference(self):
        self.assertEqual(self.calculator.calculate_difference(15, 15), 0)
    def test_negative_difference(self):
        self.assertEqual(self.calculator.calculate_difference(5, 10), -5)
        self.assertEqual(self.calculator.calculate_difference(10, 15), -5)
    def test_difference_with_negative_inputs(self):
        self.assertEqual(self.calculator.calculate_difference(-5, 10), -15)
        self.assertEqual(self.calculator.calculate_difference(10, -5), 15)
        self.assertEqual(self.calculator.calculate_difference(-5, -10), 5)
    def test_both_negative(self):
        self.assertEqual(self.calculator.calculate_difference(-10, -5), -5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)