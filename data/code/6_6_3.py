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
    def test_equal_weights(self):
        self.assertEqual(self.calculator.calculate_difference(75, 75), 0)
    def test_negative_difference(self):
        self.assertEqual(self.calculator.calculate_difference(50, 100), -50)
        self.assertEqual(self.calculator.calculate_difference(10, 50), -40)
    def test_both_negative_weights(self):
        self.assertEqual(self.calculator.calculate_difference(-10, -5), -5)
        self.assertEqual(self.calculator.calculate_difference(-100, -50), -50)
    def test_one_negative_one_positive(self):
        self.assertEqual(self.calculator.calculate_difference(10, -5), 15)
        self.assertEqual(self.calculator.calculate_difference(-10, 5), -15)
    def test_both_negative_large(self):
        self.assertEqual(self.calculator.calculate_difference(-1000, -500), -500)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)