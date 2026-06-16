import unittest
class WeightSystem:
    def __init__(self):
        pass
    def convert_to_pounds(self, weight_kg):
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative")
        return weight_kg * 2.20462
    def convert_to_grams(self, weight_lbs):
        if weight_lbs < 0:
            raise ValueError("Weight cannot be negative")
        return weight_lbs * 453.592
class TestWeightSystem(unittest.TestCase):
    def setUp(self):
        self.ws = WeightSystem()
    def test_convert_to_pounds_positive(self):
        self.assertAlmostEqual(self.ws.convert_to_pounds(10), 22.0462)
        self.assertAlmostEqual(self.ws.convert_to_pounds(0), 0.0)
    def test_convert_to_pounds_zero_edge_case(self):
        self.assertEqual(self.ws.convert_to_pounds(0), 0.0)
    def test_convert_to_pounds_negative_error(self):
        with self.assertRaisesRegex(ValueError, "Weight cannot be negative"):
            self.ws.convert_to_pounds(-10)
    def test_convert_to_grams_positive(self):
        self.assertAlmostEqual(self.ws.convert_to_grams(1), 453.592)
        self.assertAlmostEqual(self.ws.convert_to_grams(2.5), 1133.98)
    def test_convert_to_grams_zero_edge_case(self):
        self.assertEqual(self.ws.convert_to_grams(0), 0.0)
    def test_convert_to_grams_negative_error(self):
        with self.assertRaisesRegex(ValueError, "Weight cannot be negative"):
            self.ws.convert_to_grams(-1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)