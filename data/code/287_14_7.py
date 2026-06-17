import unittest
class WeightSystemConverter:
    def convert_lbs_to_kg(self, pounds):
        if not isinstance(pounds, (int, float)):
            raise TypeError("Input must be a number")
        return pounds * 0.453592
    def convert_kg_to_lbs(self, kilograms):
        if not isinstance(kilograms, (int, float)):
            raise TypeError("Input must be a number")
        return kilograms / 0.453592
class TestWeightSystemConverter(unittest.TestCase):
    def setUp(self):
        self.converter = WeightSystemConverter()
    def test_lbs_to_kg_positive_value(self):
        pounds = 10
        expected_kg = 4.53592
        self.assertAlmostEqual(self.converter.convert_lbs_to_kg(pounds), expected_kg)
    def test_lbs_to_kg_zero_value(self):
        pounds = 0
        expected_kg = 0.0
        self.assertAlmostEqual(self.converter.convert_lbs_to_kg(pounds), expected_kg)
    def test_lbs_to_kg_float_value(self):
        pounds = 150.5
        expected_kg = 68.1310969
        self.assertAlmostEqual(self.converter.convert_lbs_to_kg(pounds), expected_kg)
    def test_kg_to_lbs_positive_value(self):
        kilograms = 10
        expected_lbs = 22.0468407
        self.assertAlmostEqual(self.converter.convert_kg_to_lbs(kilograms), expected_lbs)
    def test_kg_to_lbs_zero_value(self):
        kilograms = 0
        expected_lbs = 0.0
        self.assertAlmostEqual(self.converter.convert_kg_to_lbs(kilograms), expected_lbs)
    def test_error_non_numeric_input_lbs(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg("abc")
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg[None]
    def test_error_non_numeric_input_kg(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs(None)
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs([1, 2])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)