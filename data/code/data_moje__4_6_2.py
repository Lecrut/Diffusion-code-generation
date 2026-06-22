import unittest

class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_kilometers': 0.001,
            'meters_to_miles': 0.000621371,
            'meters_to_feet': 3.28084,
            'kilometers_to_meters': 1000,
            'kilometers_to_miles': 0.621371,
            'kilometers_to_feet': 3280.84,
            'miles_to_meters': 1609.34,
            'miles_to_kilometers': 1.60934,
            'miles_to_feet': 5280,
            'feet_to_meters': 0.3048,
            'feet_to_kilometers': 0.0003048,
            'feet_to_miles': 0.000189394
        }

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value cannot be negative")
        
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit == to_unit:
            return value
        
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        
        base_value = self._to_base(value, from_unit)
        result = self._from_base(base_value, to_unit)
        return result

    def _to_base(self, value, unit):
        unit_map = {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34,
            'feet': 0.3048
        }
        return value * unit_map[unit]

    def _from_base(self, value, unit):
        unit_map = {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084
        }
        return value * unit_map[unit]

class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()

    def test_meters_to_kilometers(self):
        result = self.converter.convert(1000, 'meters', 'kilometers')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_meters_to_miles(self):
        result = self.converter.convert(1609.34, 'meters', 'miles')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_meters_to_feet(self):
        result = self.converter.convert(1, 'meters', 'feet')
        self.assertAlmostEqual(result, 3.28084, places=5)

    def test_kilometers_to_meters(self):
        result = self.converter.convert(1, 'kilometers', 'meters')
        self.assertAlmostEqual(result, 1000.0, places=5)

    def test_kilometers_to_miles(self):
        result = self.converter.convert(1, 'kilometers', 'miles')
        self.assertAlmostEqual(result, 0.621371, places=6)

    def test_kilometers_to_feet(self):
        result = self.converter.convert(1, 'kilometers', 'feet')
        self.assertAlmostEqual(result, 3280.84, places=2)

    def test_miles_to_meters(self):
        result = self.converter.convert(1, 'miles', 'meters')
        self.assertAlmostEqual(result, 1609.34, places=2)

    def test_miles_to_kilometers(self):
        result = self.converter.convert(1, 'miles', 'kilometers')
        self.assertAlmostEqual(result, 1.60934, places=5)

    def test_miles_to_feet(self):
        result = self.converter.convert(1, 'miles', 'feet')
        self.assertAlmostEqual(result, 5280, places=0)

    def test_feet_to_meters(self):
        result = self.converter.convert(1, 'feet', 'meters')
        self.assertAlmostEqual(result, 0.3048, places=4)

    def test_feet_to_kilometers(self):
        result = self.converter.convert(10000, 'feet', 'kilometers')
        self.assertAlmostEqual(result, 3.048, places=3)

    def test_feet_to_miles(self):
        result = self.converter.convert(5280, 'feet', 'miles')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_same_unit_conversion(self):
        result = self.converter.convert(50, 'meters', 'meters')
        self.assertEqual(result, 50)

    def test_case_insensitivity(self):
        result = self.converter.convert(1, 'METERS', 'Kilometers')
        self.assertAlmostEqual(result, 0.001, places=6)

    def test_negative_value_raises_error(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-10, 'meters', 'kilometers')

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            self.converter.convert("10", 'meters', 'kilometers')

    def test_invalid_unit_raises_error(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'inches', 'feet')

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(5, 'miles', 'kilometers'))
    print(converter.convert(100, 'feet', 'meters'))
    print(converter.convert(1, 'kilometers', 'miles'))
    unittest.main()