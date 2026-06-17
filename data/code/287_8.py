import unittest
class WeightSystem:
    def __init__(self):
        pass
    def convert_to_pounds(self, weight_kg):
        if weight_kg is None:
            raise ValueError("Input weight cannot be None")
        return weight_kg * 2.20462
    def convert_to_grams(self, weight_lbs):
        if weight_lbs is None:
            raise ValueError("Input weight cannot be None")
        return weight_lbs * 453.592
class TestWeightSystem(unittest.TestCase):
    def setUp(self):
        self.system = WeightSystem()
    def test_convert_to_pounds_standard(self):
        self.assertAlmostEqual(self.system.convert_to_pounds(10), 22.0462)
        self.assertAlmostEqual(self.system.convert_to_pounds(0), 0.0)
        self.assertAlmostEqual(self.system.convert_to_pounds(2.20462), 5.0)
    def test_convert_to_pounds_edge_cases(self):
        self.assertAlmostEqual(self.system.convert_to_pounds(0.0), 0.0)
        self.assertAlmostEqual(self.system.convert_to_pounds(-5), -11.0231)
    def test_convert_to_pounds_error_handling(self):
        with self.assertRaisesRegex(ValueError, "Input weight cannot be None"):
            self.system.convert_to_pounds(None)
    def test_convert_to_grams_standard(self):
        self.assertAlmostEqual(self.system.convert_to_grams(1), 453.592)
        self.assertAlmostEqual(self.system.convert_to_grams(2.20462), 999.9847808)
    def test_convert_to_grams_edge_cases(self):
        self.assertAlmostEqual(self.system.convert_to_grams(0), 0.0)
        self.assertAlmostEqual(self.system.convert_to_grams(-1), -453.592)
    def test_convert_to_grams_error_handling(self):
        with self.assertRaisesRegex(ValueError, "Input weight cannot be None"):
            self.system.convert_to_grams(None)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)