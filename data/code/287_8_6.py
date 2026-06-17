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
        self.ws = WeightSystem()
    def test_convert_to_pounds_standard(self):
        self.assertAlmostEqual(self.ws.convert_to_pounds(10), 22.0462)
        self.assertAlmostEqual(self.ws.convert_to_pounds(0), 0.0)
        self.assertAlmostEqual(self.ws.convert_to_pounds(100), 220.462)
    def test_convert_to_pounds_zero_edge_case(self):
        self.assertEqual(self.ws.convert_to_pounds(0), 0.0)
    def test_convert_to_pounds_none_error(self):
        with self.assertRaisesRegex(ValueError, "Input weight cannot be None"):
            self.ws.convert_to_pounds(None)
    def test_convert_to_grams_standard(self):
        self.assertAlmostEqual(self.ws.convert_to_grams(1), 453.592)
        self.assertAlmostEqual(self.ws.convert_to_grams(2), 907.184)
        self.assertAlmostEqual(self.ws.convert_to_grams(0), 0.0)
    def test_convert_to_grams_zero_edge_case(self):
        self.assertEqual(self.ws.convert_to_grams(0), 0.0)
    def test_convert_to_grams_none_error(self):
        with self.assertRaisesRegex(ValueError, "Input weight cannot be None"):
            self.ws.convert_to_grams(None)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)