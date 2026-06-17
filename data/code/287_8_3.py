import unittest
class WeightSystem:
    def __init__(self):
        pass
    def convert_to_kg(self, weight_lbs):
        if weight_lbs < 0:
            raise ValueError("Weight cannot be negative")
        return weight_lbs * 0.453592
    def convert_to_grams(self, weight_kg):
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative")
        return weight_kg * 1000
class TestWeightSystem(unittest.TestCase):
    def setUp(self):
        self.ws = WeightSystem()
    def test_convert_to_kg_positive(self):
        weight_lbs = 150.0
        expected_kg = 68.0388
        self.assertAlmostEqual(self.ws.convert_to_kg(weight_lbs), expected_kg)
    def test_convert_to_kg_zero(self):
        weight_lbs = 0.0
        expected_kg = 0.0
        self.assertEqual(self.ws.convert_to_kg(weight_lbs), expected_kg)
    def test_convert_to_kg_small_value(self):
        weight_lbs = 1.0
        expected_kg = 0.453592
        self.assertAlmostEqual(self.ws.convert_to_kg(weight_lbs), expected_kg)
    def test_convert_to_kg_negative_error(self):
        with self.assertRaisesRegex(ValueError, "Weight cannot be negative"):
            self.ws.convert_to_kg(-10.0)
    def test_convert_to_grams_positive(self):
        weight_kg = 5.5
        expected_grams = 5500.0
        self.assertEqual(self.ws.convert_to_grams(weight_kg), expected_grams)
    def test_convert_to_grams_zero(self):
        weight_kg = 0.0
        expected_grams = 0.0
        self.assertEqual(self.ws.convert_to_grams(weight_kg), expected_grams)
    def test_convert_to_grams_large_value(self):
        weight_kg = 100.0
        expected_grams = 100000.0
        self.assertEqual(self.ws.convert_to_grams(weight_kg), expected_grams)
    def test_convert_to_grams_negative_error(self):
        with self.assertRaisesRegex(ValueError, "Weight cannot be negative"):
            self.ws.convert_to_grams(-5.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)