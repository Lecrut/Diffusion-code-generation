import unittest
class WeightSystem:
    def __init__(self):
        pass
    def convert_to_kg(self, weight_value, unit):
        if unit == 'kg':
            return weight_value
        elif unit == 'lb':
            return weight_value * 0.453592
        else:
            raise ValueError("Invalid unit specified")
    def convert_to_lbs(self, weight_value, unit):
        if unit == 'lbs':
            return weight_value
        elif unit == 'kg':
            return weight_value / 0.453592
        else:
            raise ValueError("Invalid unit specified")
class TestWeightSystem(unittest.TestCase):
    def setUp(self):
        self.ws = WeightSystem()
    def test_convert_to_kg_valid(self):
        self.assertEqual(self.ws.convert_to_kg(10, 'kg'), 10)
        self.assertEqual(self.ws.convert_to_kg(0, 'kg'), 0)
        self.assertEqual(self.ws.convert_to_kg(15.5, 'kg'), 15.5)
    def test_convert_to_kg_invalid_unit(self):
        with self.assertRaisesRegex(ValueError, "Invalid unit specified"):
            self.ws.convert_to_kg(10, 'ton')
        with self.assertRaisesRegex(ValueError, "Invalid unit specified"):
            self.ws.ws.convert_to_kg(10, 'gram')
    def test_convert_to_lbs_valid(self):
        self.assertEqual(self.ws.convert_to_lbs(50, 'lbs'), 50)
        expected_lbs = 10 * 2.2046226
        self.assertAlmostEqual(self.ws.convert_to_lbs(10, 'kg'), expected_lbs)
        self.assertEqual(self.ws.convert_to_lbs(0, 'kg'), 0)
    def test_convert_to_lbs_invalid_unit(self):
        with self.assertRaisesRegex(ValueError, "Invalid unit specified"):
            self.ws.convert_to_lbs(10, 'ton')
        with self.assertRaisesRegex(ValueError, "Invalid unit specified"):
            self.ws.ws.convert_to_lbs(10, 'gram')
    def test_conversion_roundtrip(self):
        initial_kg = 5.0
        converted_lbs = self.ws.convert_to_lbs(initial_kg, 'kg')
        expected_kg = converted_lbs * 0.453592
        self.assertAlmostEqual(expected_kg, initial_kg)
        initial_lbs = 100.0
        converted_kg = self.ws.convert_to_kg(initial_lbs, 'lbs')
        expected_lbs = converted_kg * 0.453592
        self.assertAlmostEqual(expected_lbs, initial_lbs)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)