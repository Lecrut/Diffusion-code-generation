import unittest
class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return weight1 - weight2
class TestWeightCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = WeightCalculator()
    def test_positive_weights(self):
        self.assertEqual(self.calculator.calculate_difference(100, 50), 50)
        self.assertEqual(self.calculator.calculate_difference(200, 150), 50)
        self.assertEqual(self.calculator.calculate_difference(10, 0), 10)
    def test_zero_involvement(self):
        self.assertEqual(self.calculator.calculate_difference(50, 0), 50)
        self.assertEqual(self.calculator.calculate_difference(0, 100), -100)
        self.assertEqual(self.calculator.calculate_difference(0, 0), 0)
    def test_negative_weights(self):
        self.assertEqual(self.calculator.calculate_difference(-10, -5), -5)
        self.assertEqual(self.calculator.calculate_difference(-100, -50), -50)
        self.assertEqual(self.calculator.calculate_difference(-10, 0), -10)
        self.assertEqual(self.calculator.calculate_difference(0, -100), 100)
    def test_mixed_signs(self):
        self.assertEqual(self.calculator.calculate_difference(100, -50), 150)
        self.assertEqual(self.calculator.calculate_difference(-100, 50), -150)
        self.assertEqual(self.calculator.calculate_difference(-100, -50), -50)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)