import unittest

class DistanceConverter:
    def __init__(self):
        self.factors = {
            ('meters', 'kilometers'): 0.001,
            ('kilometers', 'meters'): 1000,
            ('meters', 'centimeters'): 100,
            ('centimeters', 'meters'): 0.01,
            ('meters', 'millimeters'): 1000,
            ('millimeters', 'meters'): 0.001,
            ('kilometers', 'miles'): 0.621371,
            ('miles', 'kilometers'): 1.609344,
            ('meters', 'feet'): 3.28084,
            ('feet', 'meters'): 0.3048,
            ('inches', 'meters'): 0.0254,
            ('meters', 'inches'): 39.3701,
            ('yards', 'meters'): 0.9144,
            ('meters', 'yards'): 1.09361,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if (from_unit, to_unit) in self.factors:
            return value * self.factors[(from_unit, to_unit)]
        
        if (to_unit, from_unit) in self.factors:
            return value / self.factors[(to_unit, from_unit)]
        
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported")

class TestDistanceConverter(unittest.TestCase):
    def test_meters_to_kilometers(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1000, 'meters', 'kilometers'), 1.0)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1.5, 'kilometers', 'meters'), 1500.0)

    def test_meters_to_centimeters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(2, 'meters', 'centimeters'), 200.0)

    def test_centimeters_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(150, 'centimeters', 'meters'), 1.5)

    def test_meters_to_millimeters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'meters', 'millimeters'), 1000.0)

    def test_millimeters_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(500, 'millimeters', 'meters'), 0.5)

    def test_kilometers_to_miles(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'kilometers', 'miles'), 0.621371)

    def test_miles_to_kilometers(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'miles', 'kilometers'), 1.609344)

    def test_meters_to_feet(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'meters', 'feet'), 3.28084)

    def test_feet_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'feet', 'meters'), 0.3048)

    def test_inches_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(100, 'inches', 'meters'), 2.54)

    def test_meters_to_inches(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'meters', 'inches'), 39.3701)

    def test_yards_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'yards', 'meters'), 0.9144)

    def test_meters_to_yards(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'meters', 'yards'), 1.09361)

    def test_same_unit_conversion(self):
        converter = DistanceConverter()
        self.assertEqual(converter.convert(42, 'meters', 'meters'), 42)

    def test_invalid_conversion(self):
        converter = DistanceConverter()
        with self.assertRaises(ValueError):
            converter.convert(1, 'meters', 'seconds')

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1000, 'meters', 'kilometers'))
    print(converter.convert(1.609344, 'kilometers', 'miles'))
    print(converter.convert(12, 'inches', 'meters'))
    print(converter.convert(5, 'miles', 'kilometers'))
    unittest.main(exit=False)