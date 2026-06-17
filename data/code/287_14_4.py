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
        self.tolerance = 1e-6
    def test_lbs_to_kg_standard_conversion(self):
        pounds = 10
        expected_kg = 4.53592
        result = self.converter.convert_lbs_to_kg(pounds)
        self.assertAlmostEqual(result, expected_kg, delta=self.tolerance)
    def test_lbs_to_kg_zero_value(self):
        pounds = 0
        expected_kg = 0.0
        result = self.converter.convert_lbs_to_kg(pounds)
        self.assertAlmostEqual(result, expected_kg, delta=self.tolerance)
    def test_lbs_to_kg_non_zero_value(self):
        pounds = 150.67
        expected_kg = 68.0384192
        result = self.converter.convert_lbs_to_kg(pounds)
        self.assertAlmostEqual(result, expected_kg, delta=self.tolerance)
    def test_kg_to_lbs_standard_conversion(self):
        kilograms = 10
        expected_lbs = 22.04672
        result = self.converter.convert_kg_to_lbs(kilograms)
        self.assertAlmostEqual(result, expected_lbs, delta=self.tolerance)
    def test_kg_to_lbs_zero_value(self):
        kilograms = 0
        expected_lbs = 0.0
        result = self.converter.convert_kg_to_lbs(kilograms)
        self.assertAlmostEqual(result, expected_lbs, delta=self.tolerance)
    def test_kg_to_lbs_non_zero_value(self):
        kilograms = 2.204672
        expected_lbs = 10.0
        result = self.converter.convert_kg_to_lbs(kilograms)
        self.assertAlmostEqual(result, expected_lbs, delta=self.tolerance)
    def test_error_handling_non_numeric_input_lbs(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg("abc")
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg([10])
    def test_error_handling_non_numeric_input_kg(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs(None)
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs({"kg": 5})
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)