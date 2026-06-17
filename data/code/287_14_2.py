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
    def test_lbs_to_kg_standard(self):
        self.assertAlmostEqual(self.converter.convert_lbs_to_kg(10), 4.53592)
        self.assertAlmostEqual(self.converter.convert_lbs_to_kg(2.20462), 1.0)
    def test_lbs_to_kg_zero(self):
        self.assertEqual(self.converter.convert_lbs_to_kg(0), 0.0)
    def test_kg_to_lbs_standard(self):
        self.assertAlmostEqual(self.converter.convert_kg_to_lbs(1), 2.20462)
        self.assertAlmostEqual(self.converter.convert_kg_to_lbs(2.20462), 1.0)
    def test_kg_to_lbs_zero(self):
        self.assertEqual(self.converter.convert_kg_to_lbs(0), 0.0)
    def test_error_non_numeric_input_lbs(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg("abc")
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_lbs_to_kg([10])
    def test_error_non_numeric_input_kg(self):
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs(3.5)
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.converter.convert_kg_to_lbs({"value": 3.5})
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)