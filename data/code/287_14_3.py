import unittest
class WeightSystemConverter:
    def to_kg(self, pounds):
        if not isinstance(pounds, (int, float)):
            raise TypeError("Input must be a number")
        return pounds * 0.453592
    def to_lbs(self, kilograms):
        if not isinstance(kilograms, (int, float)):
            raise TypeError("Input must be a number")
        return kilograms / 0.453592
class TestWeightSystemConverter(unittest.TestCase):
    def setUp(self):
        self.converter = WeightSystemConverter()
    def test_pound_to_kilogram_conversion(self):
        self.assertAlmostEqual(self.converter.to_kg(1), 0.453592)
        self.assertAlmostEqual(self.converter.to_kg(2.20462), 1.0)
    def test_kilogram_to_pound_conversion(self):
        self.assertAlmostEqual(self.converter.to_lbs(1), 2.20462)
        self.assertAlmostEqual(self.converter.to_lbs(2.20462), 1.0)
    def test_zero_value(self):
        self.assertEqual(self.converter.to_kg(0), 0.0)
        self.assertEqual(self.converter.to_lbs(0), 0.0)
    def test_float_conversion(self):
        pounds = 10.5
        expected_kg = 4.762716
        self.assertAlmostEqual(self.converter.to_kg(pounds), expected_kg)
        self.assertAlmostEqual(self.converter.to_lbs(expected_kg), pounds)
    def test_non_numeric_input_error(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.to_kg("abc")
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.to_lbs([10])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)