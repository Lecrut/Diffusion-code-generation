import unittest
class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return weight1 - weight2
class TestWeightCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = WeightCalculator()
    def test_positive_difference(self):
        self.assertEqual(self.calculator.calculate_difference(100, 50), 50)
    def test_negative_difference(self):
        self.assertEqual(self.calculator.calculate_difference(50, 100), -50)
    def test_zero_difference(self):
        self.assertEqual(self.calculator.calculate_difference(75, 75), 0)
    def test_identical_weights(self):
        self.assertEqual(self.calculator.calculate_difference(200, 200), 0)
    def test_large_numbers(self):
        self.assertEqual(self.calculator.calculate_difference(1000000, 100000), 900000)
    def test_negative_inputs(self):
        self.assertEqual(self.calculator.calculate_difference(-10, 5), -15)
        self.assertEqual(self.calculator.calculate_difference(10, -5), 15)
        self.assertEqual(self.calculator.calculate_difference(-10, -5), -5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)